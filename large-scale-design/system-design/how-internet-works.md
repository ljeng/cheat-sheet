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

| Alternative | Best use case | Limitations |
| --- | --- | --- |
| **load balancers** | simple SOA environments with short-lived connections | you don't have long-lived connections |
| **standard DNS** | read-optimized, the results are a little stale | doesn't scale as well because every time you add new machines, you're updating data in your DNS server |
| **databases** | storing static configuration | adds load to the DB sans ordering guarantees |

The **Raft consensus algorithm** inspired a new generation of coordination tools that are easier to implement than ZooKeeper’s ZAB protocol.

| **etcd** | a distributed key-value store for service discovery[^2] |
| **Consul** | a highly featured service discovery and configuration system |
| **Serf** | a communication protocol you can build things on top of |

Not to diss these, but Zookeeper has had a long time to get to the place where bugs are relatively rare. If you're interested in something stodgy and boring, use one of the 3.4 releases.

I care about **operational overhead**. A DNS is an option for a simple environment. ZooKeeper is the most reliable, crufty option out there. 3.5 has dynamic reconfig.

## Load Balancers

## Firewalls

[^1]: a DNS replacement
[^2]: Kubernetes
