# How the Internet Works

## Routers

## Domain Name Servers

Service management is a category of infrastructure needs that has existed long before modern distributed systems. At its core, it manages how services interact and discover one another through well-defined configuration. Using **distributed dynamic discovery**[^1], service management also requires organizations to maintain service registries.

DNS was historically the tool for service discovery. However, Google encountered constraints as organizations scaled. DNS didn't cope well with the rapid churn of thousands of machines. DNS caching mechanisms mean that updates aren't instantaneous. DNS tells you what *could* be at an address, not necessarily what's currently up. To solve these issues, Google developed **Chubby**, which inspired the creation of **Apache ZooKeeper**. These tools facilitate a centralized way to track which machines are available and what roles they're performing in real-time.

ZooKeeper is a powerful tool, but it's misunderstood. Its utility can be broken down into two main areas:

1. You can say, "I want to know who's up right now, who's available, what machines are available doing what actions."  It's also a general **service registry**.
1. You can store configuration in ZooKeeper, and that'll let people know when configuration changes so they can automatically update themselves.

Not a monitoring solution per se, ZooKeeper is effective for liveness checks. If a system only needs to know a few critical facts about the environment’s health, ZooKeeper's ephemeral nodes provide a reliable heartbeat mechanism.

ZooKeeper operates under architectural constraints that dictate its performance guarantees. ZooKeeper keeps its entire state **in memory** to avoid Java Garbage Collection (GC) pauses. A stop-the-world GC event can break heartbeats, precipitating quorum loss. ZooKeeper is a key-value store for metadata, not large datasets. It's not a distributed cache. ZooKeeper can technically facilitate messaging, but it's not a dedicated **pub-sub** system. RabbitMQ is more appropriate for high-volume messaging.

Depending on the complexity of the environment, ZooKeeper may be overkill. Alternatives exist.

| Alternative    | Best use case                      | Limitations                                                       |
| ---------- | -------------------------------- | --- |
| **load balancers** | simple SOA environments with short-lived connections | you don't have long-lived connections                               |
| **standard DNS**  | read-optimized, the results are a little stale    | doesn't scale as well because every time you add new machines, you're updating data in your DNS server |
| **databases**   | storing static configuration              | adds load to the DB sans ordering guarantees                                   |

The **Raft consensus algorithm** inspired a new generation of coordination tools that are easier to implement than ZooKeeper’s ZAB protocol.

| **etcd**  | a distributed key-value store for service discovery[^2]    |
| **Consul** | a highly featured service discovery and configuration system |
| **Serf**  | a communication protocol you can build things on top of    |

Not to diss these, but Zookeeper has had a long time to get to the place where bugs are relatively rare. If you're interested in something stodgy and boring, use one of the 3.4 releases.

I care about **operational overhead**. A DNS is an option for a simple environment. ZooKeeper is the most reliable, crufty option out there. 3.5 has dynamic reconfig.

## Load Balancers

Load balancing distributes the work across multiple consumers in message-oriented middleware. There are two patterns for achieving this:

- Each message is delivered to exactly one consumer in a consumer group, while multiple consumers can collaborate to share the workload of a single topic. The broker assigns messages to consumers arbitrarily. This pattern is useful when messages are computationally expensive to process and you need to scale horizontally by adding more consumers.

| *Implementation* | *Known as*                 |
| **AMQP**     | multiple clients consuming from the same queue |
| **JMS**     | a shared subscription                   |

- Unlike the competing consumers pattern, a log-based broker supports fan-out messaging because multiple consumers read the log independently without deleting messages. The broker assigns entire **partitions** to nodes within a consumer group rather than assigning individual messages to achieve load balancing here.

The number of consumers can't exceed the number of log partitions, as each partition is assigned to only one node. A single slow message can delay all subsequent messages in that partition because messages within a partition are processed sequentially[^3].

Load balancing requires care; implementing it in shared-memory parallel systems using threads is notoriously error-prone due to **dynamic work partitioning**. It's complicated to divide tasks so that every thread receives an approximately equal load. Programmers must implement communication protocols for most applications to prevent some threads from idling while others are overwhelmed.

We look at the absolute worst case when analyzing the efficiency of these systems. We apply load balancing to avoid both underutilization and overload, improving overall performance. A task-parallel scheduler must operate **online**, meaning it makes scheduling decisions without knowing in advance when procedures will be spawned or when they will finish. Threads cooperate to balance the load in a real-world distributed fashion. Provably good **distributed schedulers** exist; they're mathematically tractable to analyze. We use an online **centralized scheduler** for the sake of simplicity in analysis. This model assumes a global knowledge of the computation state at any given moment, providing a clearer baseline for performance evaluation.


## Firewalls

[^1]: a DNS replacement
[^2]: Kubernetes
[^3]: single-threaded
