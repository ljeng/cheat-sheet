# Distributed Systems

## The Reality: From Theory to Architecture

<blockquote>
	Hey I just met you
	The network's laggy
	But here's my data
	So store it maybe
</blockquote>

— <cite>Kyle Kingsbury, *Carly Rae Jepsen and the Perils of Network Partitions* (2013)</cite>

We move from single-node systems to distributed architectures. We must shift our mindset from optimism to extreme pessimism. Anything that can go wrong, will go wrong. Experienced operators assume this. It's no longer enough to ask if a disk is working. We must account for semi-failures - where a disk is slow but not dead or a network is dropping 10% of packets.

❌ There's a common mathematical argument for reliability. If a node has a probability $P$ of failure, and you have $N$ replicas, the probability of total failure is $P^N$.

✅ A specific poison pill request crashes one kernel. It'll likely crash them all.

True reliability isn't a theoretical calculation. It's empirical.

"Service-oriented architecture" evokes memories of bloated legacy standards and nebulous architectures, but the idea remains the gold standard: loosely coupled services, each performing a discrete function with independent fault domains. You must address these three pillars when defining a service within a distributed system:

1. Is the service global or regional?
2. Is it single-tenant or multi-tenant?
3. What are the guarantees for availability, latency, throughput, consistency, and durability?

To illustrate these principles, consider a service that resizes images. Although it seems trivial, operating this at scale disabuses engineers of any optimism; the inherent complexity of distributed systems is ineluctable.

100,000 users; 10,000 requests per second (RPS) per region -> an average image is 256KB. A single CPU core handles 10 conversions per second.

1. We need at least three servers[^1]. They handle the 10k RPS load with 5k RPS per server.
1. We need a buffer because there's a scale discrepancy between the fast API servers and the slower processing cores. We must choose between consistency and availability according to the CAP theorem. Most queues prioritize **consistency**[^2]. We must automate leader election and failover using Paxos or Raft to meet high availability. Manual failover is too slow to meet a 99.9% SLA.
1. Customer management[^3] happens rarely, but **authentication** happens on every request. We decouple the management plane from the data plane. We cache **identity** data at the edge. This favors **availability** over **consistency**[^4], but the system must remain fast.
1. **Usage** tracking is the inverse of the API: it's read-light. Perform local aggregation of logs on the API servers, then ship them in batches to an eventually consistent store[^5]. Use a MapReduce or batch-processing system to aggregate this data for billing and move raw records to cold storage[^6] for compliance.

Distributed systems are the future of scaling. But we must move past irrational exuberance. It takes a decade for a filesystem to be considered stable. Cassandra requires years of operational scars to reach reliability. Building a distributed system isn't just about writing code. It's about building a system that can survive the messy reality of the physical world.

[^1]: plus headroom
[^2]: FIFO ordering
[^3]: creating accounts
[^4]: a new user might have to wait a few seconds before his credentials work
[^5]: a Dynamo-style key-value store
[^6]: tape or low-cost disk
