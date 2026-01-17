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
