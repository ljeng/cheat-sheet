# Distributed Systems

## The Reality: From Theory to Architecture

<blockquote>
	Hey I just met you
	The network's laggy
	But here's my data
	So store it maybe
</blockquote>

— <cite>**Kyle Kingsbury**, *Carly Rae Jepsen and the Perils of Network Partitions* (2013)</cite>

A recurring theme is how systems handle things going wrong - for example, replica failover, replication lag, and concurrency control. Working with distributed systems is fundamentally different from writing software on a single computer. We'll now turn our pessimism to the max. Experienced operators assume that anything that can go wrong will go wrong. Dealing with failures explodes the possible state space that needs testing and validation. It doesn't make sense to expect a single-node database to be fast if its disk system gets really slow. Semi-failures are common. The core argument that gets used for these systems is that if a node has a probability $P$ of failure and if the software can replicate data $N$ times to survive $N - 1$ failures, then the probability of losing a particular piece of data is $P^N$. So for any desired reliability $R$ and any single-node failure probability $P$, you can pick some replication $N$ so that

$$P^N < R$$

**which is hogwash**. The reasoning assumes failures are independent. Failures are correlated. Identical hardware runs on the same power supply. The same bug exists on all the machines. One client sends corrupt requests; it's able to sequentially bring down all the servers. When you push the **bad config**, it's game over no matter how many machines you push it to. There's really only one thing to talk about with respect to reliabiity: continuous hours of successful production operations. I call this **empirical** reliability[^01].

A common term that applies to distributed-system architecture is service-oriented architecture (SOA). While SOA may conjure memories of WS-standards and the nebulous Common Object Request Broker Architecture, the core idea is solid: loosely coupled services, each serving a small function and working independently from one another.
For each of the services identified, you must consider the following items:

1. Is the service global or regional?
1. Is it single-tenant or multi-tenant?
1. What are the guarantees for availability, latency, throughput, consistency, and durability?
1. How is IAAA (identity, authentication, authorization, and audit) considered?
1. How is billing for quota limits performed?
1. How will updates to the system be deployed?

To illustrate these principles, consider a service that resizes images. Although it seems trivial, operating this at scale disabuses engineers of any optimism; the inherent complexity of distributed systems is ineluctable.

100K users; 10K requests per second (RPS) per region. The 99<superscript>th</superscript> %ile of latency should <500ms for images <1MB in size. The system provides 99.9% availability. The service should offer a usage-based pricing model[^02], so it needs to keep track of the amount of CPU time required to convert an image and its size.

Assume an average of 256KB per image, so the system can process 10 conversions per second per CPU core. We need **1K cores** to support 10K RPS. We need ~32 servers using 32-core machines. Adding 20% headroom for surges, we require a fleet of $\geq 40$ **dedicated processing systems**. This scale confirms that a simple single-server monolith is impossible; we need a distributed stack.

Figure 1 breaks the system down into a few coarse services:

```mermaid
graph TB
    subgraph TOP_ROW [ ]
        direction LR
        style TOP_ROW fill:none,stroke:none
        subgraph QL ["Queue Layer<br/>Consistency Priority"]
            direction TB
            Q1[Queue Node 1<br/>Leader]
            Q2[Queue Node 2<br/>Follower]
            Q3[Queue Node 3<br/>Follower]
            PAXOS[Paxos consensus<br/>Auto failover]
        end
        subgraph API_TIER ["Customer-facing API Tier<br/>99.99% availability"]
            direction TB
            LB[Load balancer<br/>10K RPS total]
            API1[API server 1<br/>5K RPS]
            API2[API server 2<br/>5K RPS]
            API3[API server 3+<br/>Buffer capacity]
        end
    end
    subgraph MID_ROW [ ]
        direction LR
        style MID_ROW fill:none,stroke:none
        subgraph AUTH ["Identity & Auth<br/>Availability Priority"]
            direction TB
            EDGE[Edge cache<br/>Identity data]
            MGMT[Management plane<br/>Customer management - rare]
            DATA[Data plane<br/>Auth - every request]
        end
        subgraph USAGE ["Usage Tracking<br/>Read-light"]
            direction TB
            AGG1[Local aggregator 1]
            AGG2[Local aggregator 2]
            AGG3[Local aggregator 3]
            BATCH[Batch store<br/>Eventually consistent]
        end
    end
    subgraph PROC ["Processing & Storage"]
        direction TB
        MR[MapReduce<br/>Batch processing]
        BILL[Billing aggregation]
        COLD[Cold storage<br/>Compliance records]
    end
    LB -->|Distribute| API1
    LB -->|Distribute| API2
    LB -->|Distribute| API3
    API1 -->|Buffer for scale| Q1
    API2 -->|discrepancy| Q2
    API3 --> Q3
    PAXOS -.->|Leader election| Q1
    PAXOS -.->|Failover| Q2
    PAXOS -.->|Failover| Q3
    API1 -->|Every request| EDGE
    API2 -->|Every request| EDGE
    API3 -->|Every request| EDGE
    EDGE -.->|Cached from| DATA
    MGMT -.->|Rare updates| DATA
    API1 -->|Local logs| AGG1
    API2 -->|Local logs| AGG2
    API3 -->|Local logs| AGG3
    AGG1 -->|Batched| BATCH
    AGG2 -->|Batched| BATCH
    AGG3 -->|Batched| BATCH
    BATCH -->|Process| MR
    MR -->|Aggregate| BILL
    MR -->|Archive| COLD
    TOP_ROW ~~~ MID_ROW
    MID_ROW ~~~ PROC
    style API1 fill:#90EE90
    style API2 fill:#90EE90
    style API3 fill:#90EE90
    style Q1 fill:#FFB6C1
    style EDGE fill:#87CEEB
    style BATCH fill:#DDA0DD
    style PAXOS fill:#FFD700

```

*Figure 1*

1. Since the business wants 99.90% availability from the system, let's set a goal for the customer-facing API tier[^03] at 99.99% percent availability.
1. We need at least three servers[^04]. They handle the 10K RPS load with 5K RPS per server.
1. We need a buffer because there's a scale discrepancy between the fast API servers and the slower processing cores. We must choose between consistency and availability according to the CAP theorem. Most queues prioritize **consistency**[^05]. We must automate leader election and failover using Paxos to meet high availability. Manual failover is too slow to meet a 99.90% SLA.
1. Customer management[^06] happens rarely, but **authentication** happens on every request. We decouple the management plane from the data plane. We cache **identity** data at the edge. This favors **availability** over **consistency**[^07], but the system must remain fast.
1. **Usage** tracking is the inverse of the API: it's read-light. Perform local aggregation of logs on the API servers, then ship them in batches to an eventually consistent store[^08]. Use a MapReduce or batch-processing system to aggregate this data for billing and move raw records to cold storage[^09] for compliance.

Distributed systems are the default approach to scaling, but no one benefits from irrational exuberance. It takes about a decade for a file system to mature. Good software can't run reliably with bad **operations**. Check invariants[^10]. If you have a NoSQL vendor, ask for the observed real-life distribution of MTTF and MTTR.

## Engineering

When you're writing a program on a single computer, it behaves predictably: it either works or it doesn’t. The same operation produces the same result[^11] if the hardware is working correctly. If there's a hardware problem (e.g., memory corruption), the consequence is usually a total system failure[^12]. An individual computer is either fully functional or entirely broken. In distributed systems, we're no longer operating in an idealized system model. We confront the messy reality of the physical world when you're writing software that runs on several computers connected by a network. What sets distributed systems engineering apart is the **probability of partial failure**. If a mutex unlock fails, we can assume the process is unstable and crash it. But the failure of a distributed unlock must be built into the lock protocol. You may not even know whether something succeeded, as the time it takes for a message to travel across a network is non-deterministic!

I've seen a number of distributed databases describe themselves as being CA[^13] while not providing partition-tolerance - a solecism that indicates that the developers don't understand the CAP theorem. Under the **consistency** guarantee[^14], each operation looks as if it were completed at a single instant. This is equivalent to requiring requests of the distributed shared memory to act as if they were executing on a single node. For a distributed system to be **available**, every request received by a non-failing node must result in a response[^15].

```mermaid
graph TD
    subgraph S1 ["Normal Network Operation"]
        N1[Node 1]
        N2[Node 2]
        N3[Node 3]
        N1 -.->|message| N2
        N2 -.->|message| N3
        N3 -.->|message| N1
    end
    S1 --> S2
    subgraph S2 ["Network Partition<br />Messages Lost"]
        P1[Node 1]
        P2[Node 2]
        P3[Node 3]
        P1 -.->|❌ lost| P2
        P2 -->|✅ delivered| P3
        P3 -.->|❌ lost| P1
        P1 -.->|❌ lost| P3
    end
    S2 --> S3
    subgraph S3 ["Partition Tolerance Property"]
        PT[System continues operating despite arbitrary message loss]
    end
    style N1 fill:#90EE90
    style N2 fill:#90EE90
    style N3 fill:#90EE90
    style P1 fill:#FFB6C6
    style P2 fill:#FFB6C6
    style P3 fill:#FFB6C6
    style PT fill:#87CEEB

```

*Figure 2*

When a network is partitioned, all messages sent from nodes in one component of the partition to nodes in another component are lost.

**You can't choose CA** for a distributed system. It would need to run on a network which is guaranteed to never drop messages and whose nodes are guaranteed to never die. These types of systems don't exist.

Atomic consistency is expected by most web services. That said, the universe doesn't permit consistency which is both instantaneous and global. Information has an upper limit to the speed it can travel[^16]. The goal is to push consistency breaks down to a point where we no longer notice it. Just don't try to act outside your own light cone. The trick of horizontal scalability is **independence**.

```mermaid
graph TD
    subgraph S1["1 Machine"]
        M1[Machine] --> D1[Decision Made ✅]
        style M1 fill:#90EE90
        style D1 fill:#90EE90
    end
    S1 --> L1[Simple]
    style L1 fill:#90EE90
    L1 --> S2
    subgraph S2["2 Machines<br />Agreement Needed"]
        M2A[Machine A] -.->|propose| Agreement1[Agreement Protocol]
        M2B[Machine B] -.->|propose| Agreement1
        Agreement1 -->|consensus| D2[Decision Made ✅]
        Agreement1 -.->|network delay| Delay1[Complexity++]
        Agreement1 -.->|conflict resolution| Delay1
        style M2A fill:#FFD700
        style M2B fill:#FFD700
        style D2 fill:#FFD700
        style Delay1 fill:#FFA500
    end
    S2 --> L2[Harder]
    style L2 fill:#FFD700
    L2 --> S3
    subgraph S3["3+ Machines<br />Even Harder"]
        M3A[Machine A] -.->|propose| Agreement2[Agreement Protocol]
        M3B[Machine B] -.->|propose| Agreement2
        M3C[Machine C] -.->|propose| Agreement2
        M3D[Machine D] -.->|propose| Agreement2
        Agreement2 -->|quorum?| D3[Decision Made ✅]
        Agreement2 -.->|network partitions| Delay2[Complexity+++]
        Agreement2 -.->|Byzantine faults| Delay2
        Agreement2 -.->|split brain| Delay2
        style M3A fill:#FF6B6B
        style M3B fill:#FF6B6B
        style M3C fill:#FF6B6B
        style M3D fill:#FF6B6B
        style D3 fill:#FF6B6B
        style Delay2 fill:#DC143C
    end
    S3 --> L3[Much Harder]
    style L3 fill:#FF6B6B

```

*Figure 3*

Standard database replication isn't strongly consistent. Special logic must be introduced to handle replication lag. Paxos is very hard to implement. Avoid coordinating machines wherever possible.

Design for failure. I've dealt with switch failures, PDU failures, accidental power cycles of racks, and even a hypoglycemic driver smashing his pickup truck into a HVAC system. Backpressure is one of the basic building blocks of creating a robust distributed system. It's the signaling of failure from a serving system to the requesting system. Implementations of backpressure involve either dropping new messages or shipping errors back to users. Timeouts and exponential back-offs are essential. Without backpressure, cascading failure becomes likely.

```mermaid
graph TB
    subgraph Metrics["Latency Metrics Comparison"]
        A["Average Latency ❌"] -->|"misleading"| B["Hides outliers<br />Assumes bell curve<br/>Poor user experience insight"]
        C["Percentiles ✅"] -->|"accurate"| D["P50: Median experience<br />P99: Worst 1%<br />P99.9: Tail latency"]
        style A fill:#ffcccc
        style C fill:#ccffcc
    end
    subgraph Availability["Uptime vs Yield"]
        E["Uptime Metric"] -->|"time-based"| F["% of time system is up<br />Ignores request volume"]
        G["Yield Metric"] -->|"request-based"| H["% of requests served<br />Accounts for traffic patterns"]
        I["Example: 1 second downtime"] --> J["Off-peak: Low impact<br />Peak: High impact"]
        J --> K["Same uptime<br />Different yield"]
        style G fill:#ccffcc
        style E fill:#ffffcc
    end
    subgraph Locality["Data Locality Principle"]
        L["Processing"] -->|"close proximity"| M["Persistent Storage"]
        M -->|"efficient"| N["Pointer dereferences<br />Low latency<br />Fewer failures"]
        L -->|"network separation"| O["Remote Storage"]
        O -->|"inefficient"| P["Network calls<br />Higher latency<br />More failures"]
        style N fill:#ccffcc
        style P fill:#ffcccc
    end
    Metrics -.->|"better monitoring"| Availability
    Availability -.->|"consider traffic"| Locality
    style Metrics fill:#e3f2fd
    style Availability fill:#f3e5f5
    style Locality fill:#e8f5e9

```

*Figure 4*

**Harvest** is the fraction of the data that was reflected in the result. For example, if a search engine queries three shards[^17] but Shard B is down, returning results only from A and C gives you a **67% harvest**. A partial answer[^18] is better than no answer[^19] for many businesses.

Your system will have to make a choice between **reducing yield**[^20] and **reducing harvest**[^21]. You're always building a **partition-tolerant** system. Decide now how you'll handle the moment the lights go out.

[^01]: as opposed to theoretical reliability
[^02]: requires precise CPU/size tracking
[^03]: the front door
[^04]: plus headroom
[^05]: FIFO ordering
[^06]: creating accounts
[^07]: a new user might have to wait a few seconds before his credentials work
[^08]: a Dynamo-style key-value store
[^09]: tape or low-cost disk
[^10]: "Are all messages sent actually received?"
[^11]: determinism
[^12]: a kernel panic of Blue Screen of Death
[^13]: consistent and available
[^14]: atomic/linearizable
[^15]: not an error or timeout
[^16]: the speed of light
[^17]: A, B,and C
[^18]: reduced harvest
[^19]: reduced yield
[^20]: stop answering
[^21]: give incomplete answers
