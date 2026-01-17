# Networks

## Unreliability in Shared-nothing Systems

The distributed systems I advocate are **shared-nothing systems**: collections of machines connected by a network. The network is the sole communication channel; I assume each machine has its own disk, and one machine can't access another’s resources except by making requests over the network. This shared-nothing architecture is dominant for internet services because it's cost-effective using commoditized cloud infrastructure and achieves high reliability through redundancy. However, this reliance on the network introduces unreliability. The internet is an asynchronous **packet network**. A node can send a message[^01] to another in this model, but the network provides no guarantees about its delivery. Many things can go wrong when you send a request and expect a response. Your **request packet may be lost** in transit[^02]. Your **request** may be waiting in a queue and will be delivered later[^03]. The remote **node** may have crashed, been powered down, or become otherwise unavailable. The remote node may have paused[^04] but will resume **responding** later. The remote node may have processed your request, but **the response packet was lost** on its way back. The remote node may have processed the request, but **the response has been delayed** in transit.

### Partitions in Distributed Systems

Persistent network unreliability is so fundamental that it tops [Peter Deutsch's list of "Eight Fallacies of Distributed Computing"](https://nighthacks.com/jag/res/Fallacies.html). This is unsurprising, as distributed programs' reliance on shared network channels defines them. Distributed computing revolves around the (im)possibilities of computation under varying network conditions.

For instance, the FLP impossibility result demonstrates the inability to guarantee consensus in an asynchronous network[^05] with one faulty process. Basic operations such as modifying the set of machines in a cluster[^06] aren't guaranteed to complete in the event of network asynchrony and individual server failures. The implications aren't simply academic: these impossibility results have motivated a proliferation of systems. Under a more reliable network that guarantees timely message delivery, FLP no longer holds. These impossibility results have spurred system development. By making stronger guarantees about network behavior, we can circumvent the programmability implications of these impossibility proofs.

The degree of reliability circumscribes the kinds of operations that systems can reliably perform without waiting. Some claim that networks are reliable and that we're too concerned with designing for theoretical failure modes. This would make extensive failure-mode design unnecessary. Others surmise differently - James Hamilton of AWS summarizes, "Network partitions should be rare but net gear continues to cause more issues than it should." So who's right?

A key challenge is the privation of evidence. We have few normalized bases for comparing app reliability and even less data. We can track packet loss, but the E2E (end-to-end) effect on apps is far more elusive. The evidence is difficult to generalize: it's deployment-specific and tied to particular vendors and topologies. Organizations share specifics about their network's behavior. Finally, distributed systems resist failure, which means that noticeable outages depend on complex interactions of failure modes. Apps silently degrade when the network fails, and the resulting problems may not be understood for some time.

Much of what we believe about real-world distributed system failures is founded on guesswork. Sysadmins swap stories over beer[^07], but detailed network availability surveys are few and far between. I bring a few of these stories together. This is a step toward an open discussion of real-world partition behavior. Anecdotal evidence shows that network problems are surprisingly common, even in controlled environments like a company-operated data center. One study in a midsize data center found ~12 network faults per month, of half disconnected a single machine and the other half disconnected an entire rack. Another study measured failure rates of load balancers. It found that adding redundant netgear doesn't always palliate faults as much as hoped against human error[^08], a major cause of outages.

Public clouds services are notorious for transient network glitches, affecting a particular availability zone. Failures occur between specific subsections of the data center, revealing planes of cleavage in the underlying hardware topology. A problem during a software upgrade for a switch could trigger a network topology reconfiguration. Cloudflare deployed a new firewall rule in response to a distributed denial-of-service (DDoS) attack. Juniper routers encountered the rule and then proceeded to consume all their RAM until they crashed. Recovery was arduous. Calling on-site engineers to reboot routers takes time. Even though some data centers came back online initially, they fell back over again because all traffic in Cloudflare's entire network hit them. Recovery was complete after an hour of unavailability. wide area network (WAN) are also common. Researchers analyzed five years of operation in the Corporation for Education Network Initiatives in California WAN. They discovered more than 500 isolating network partitions. Median duration ranged from 2.7 minutes for software-related failures to 32 minutes for hardware failures and a 95th percentile of 3.7 days for hardware-related failures. There have been several global Internet outages related to BGP misconfiguration. In 2008, Pakistan Telecom, responding to an edict to block [YouTube.com](https://www.youtube.com/), incorrectly advertised its block to other providers, which hijacked traffic from the site and rendered it unreachable. Similar incidents occurred in 1997, 2005, 2006, and 2010. Sharks bite undersea fiber-optic cables. Google wrapped its trans-Pacific cables in Kevlar to guard against shark bites.

If the error handling of network fault isn't defined and tested, arbitrarily bad things could happen: the cluster could become permanently unable to serve requests, or it could delete all of your data.

> This was one of the worst outages in the history of GitHub, and it's not at all acceptable to us. I'm very sorry that it happened and our entire team is working hard to prevent similar problems in the future.

-- <cite>Mark Imbriaco, ["Downtime Last Saturday"](https://github.blog/news-insights/downtime-last-saturday/)</cite>

**The network may fail - there's no way around it.** Handling these faults doesn't always mean tolerating: if your network is normally reliable, a valid approach is to simply show an error message to users. However, you need to know how your software reacts and ensure that the system can recover. It makes sense to deliberately test the system's response[^09].

## The E2E Argument in Distributed Systems

In the CAP theorem, "partitions" connotes network partitions - not node failures. These are distinct in theory; many systems treat them as the same in practice because they're often handled with the same blunt instrument: **the timeout**. However, treating every silence as a network partition is an optimization killer. We can build responsive distributed apps by looking at how Apache HBase handles failures and applying the classic E2E argument of system design.

Zookeeper manages failures by giving the user the possibility to create ephemeral nodes. These znodes exist only as the session is active. When the session ends, the znode is deleted. Expirations happen when the cluster doesn't hear from the client within the specified timeout[^10]. The timeout represents the major cost for **MTTR** for any type of failure: process crash, node failure. The lock will be freed after 20 seconds. Network partition is an enigma. You don't know what's going on on the other side; it can be dead or not. A partition-tolerant app has to expect the worst. But a **process crash** is simpler. The node is there, hence it can communicate the process' death immediately. Since the process is dead, there's no risk of having a split brain situation. Another node can take over quickly without having to wait for a timeout to expire.

A lower-level subsystem[^11] that supports a distributed app may be wasting its effort in providing a function that must be implemented at the app level anyway. [The basic argument](https://groups.csail.mit.edu/ana/Publications/PubPDFs/End-to-End%20Arguments%20in%20System%20Design.pdf)[^12] can be applied to a variety of functions in addition to reliable data transmission. For the data communication system to go out of its way to be reliable doesn't reduce the burden on the app program to ensure reliability. Consider the problem of careful file transfer. The object is to move the file from Computer A's storage to Computer B's storage. The file may contain incorrect data, perhaps because of intermittent hardware faults in the disk storage system. The software of the file transfer program might make a mistake in buffering. The communication system might drop a packet. In order to achieve careful file transfer, the app program must supply a checksum. The question is whether or not this attempt to be helpful is useful. Communication system errors may have been eliminated, but the careful file transfer app must still counter software mistakes in the file system. The app s*hould* provide its own retries based on an E2E checksum[^13]. Thus the amount of effort to put into reliability measures is an engineering trade-off based on **performance** rather than **correctness**.

When we issue a `close()` on a TCP socket, the kernel may do exactly that; the app wants to know whether or not the target host acted on the message. The `close()` call really doesn't convey what we're trying to tell the kernel: "Please close the connection after ending all the data I submitted through `write()`." Even though your data was still waiting to be sent or not acknowledged, the kernel can close the connection. The `SO_LINGER` socket option appears to have been written with just this issue in mind. When enabled, a `close(2)` or `shutdown(2)` won't return until all queued messages for the socket have been successfully sent or the linger timeout has been reached. The acknowledgment desired is an E2E one, which can be originated only by the target app. Knowing that the message was delivered to the target host isn't very important. **Host A** calls `shutdown(sock, SHUT_WR)`, sending a FIN packet. This will lead to a FIN package being sent to **Program B**[^14]. **Program B** will in turn close down its socket, and we can detect this from **Program A**: a subsequent `read()` will return `0`[^15]. **Program A** now becomes

```c
shutdown(sock, SHUT_WR);
  for (;;) {
    res = read(sock, buffer, 4000);
    ...
    if (!res) break;
  }
  close(sock);

```

The communication system provides selective redundancy. The app must supply a file-transfer-specific, E2E reliability guarantee.

The **operating system (OS)** will send a RST or FIN packet if a process crashes but the OS survives. If a process was killed by an admin, a script can notify other nodes about the crash so that another node can take over quickly without having to wait for a timeout to expire. For example, HBase does this. If you have access to network switches, you can **query** them. Rapid feedback is useful, but you can't count on it. Even if TCP acknowledges that a packet was delivered, the app may have crashed. If you want to be sure that a request was successful, you need a **positive response from the app itself**. You can wait for a timeout to elapse and eventually declare the node dead if you don't hear back within the timeout. If the only tool you have is a timeout, then you have no information about what happened.

- Correctness belongs at the high level[^16].
- Reliability measures at the low level[^17] are performance optimizations.
- Efficiency comes from learning to distinguish between different types of failures. We sacrifice performance if we treat every silence as a network partition. We improve MTTR without compromising timeout safety for true network partitions if we use OS-level signals to detect crashes.

We can build distributed stores that are fast in the common case of a crash and correct in the rare case of a partition only if we enumerate where our system's endpoints truly lie.

## Delay and Congestion Control

We model delay using a virtual-output queued layer 2 switch in an initially idle data center network where link rates don't decrease from the edge to the core. The switch scheduler serializes arrivals when multiple input ports send packets to a single output port concurrently. A packet waits for all other input ports to be serviced in the worst case.

- *Single switch*: A packet waits for `max_fan_in - 1` packets.
- *Multi-hop network*: Treating the network as a single big switch[^18], a packet may experience interference from `n - 2` packets, where `n` is the number of hosts.

We calculate the **worst-case E2E delay** $\tau$ as

$$\tau \leq \frac{n \times P}{R} + \epsilon$$

where $n$ is the number of hosts, $P$ the maximum packet size, R is the rate of the slowest link, and $\epsilon$ is the cumulative processing delay. In a **mesochronous network**[^19], we must double this bound to account for phase misalignment $e$:

$$e = \frac{2n \times P}{R} + \epsilon$$

If all hosts are rate-limited to one packet per epoch, then most permanent queues can build up; it's quixotic to make any guarantees about delays.

The internet and most internal networks in data centers are asynchronous networks. In these environments, we can't make any guarantees about delays. If several different nodes simultaneously try to send packets to the same destination, the network switch must queue them up. If the destination machine's CPU is busy, the incoming request is queued by the **operating system** until the app is ready to handle it. A virtual machine is often paused[^20] for tens of milliseconds. During this time, the VM can't consume any data from the network. Congestion control[^21] queues data at the sender before it even enters the network. A reasonable timeout would be $2d + r$[^22]. Choosing a timeout is a trade-off. If **a timeout is low**, it detects faults sooner, but there is a higher risk of falsely declaring a node dead when it is actually just suffering from a temporary spike.  This positive feedback loop can lead to a cascading failure. If you make **the timeout long**, the system is more stable but users have to wait for a long time before they notice a failure.

The drop in throughput is a signal of congestion. A strategy is multiplicative decrease: when a packet is dropped, prune the window[^23] by a factor of 2. One each error-free round-trip, increase the window by one packet. In practice, this is done by  `cwnd += 1\cwnd` on each ACK. There's only so much that can be done at the endpoints. The gateways[^24] are the only places where the information necessary for fair sharing is available. If early congestion is caught early, small window adjustments suffice. If it's caught late, massive adjustments are required.

When $f = 1$, QJUMP provides a hard latency bound. However, the rate-limiting required for $f = 1$, the setting for guaranteed latency[^25], is very aggressive. To allow for higher throughput, QJUMP introduces a scaling factor $f$. We define the assumed number of senders as $n' = \frac{n}{f}$. When $f = n$, the rate limit is $\frac{R}{2}$ and the latency bound is the same as for standard Ethernet[^26]. Data center switches support the IEEE 802.1Q standard, which provides service classes[^27]. Existing priority mechanisms stokes a race to the top. QJUMP couples priority with rate-limiting. **High-priority** levels are given low-latency guarantees but are restricted to low throughput. **Low-priority** levels are given no latency guarantees but are allowed to use all of the remaining bandwidth[^28]. [Grosvenor, et. al.](https://dl.acm.org/doi/10.5555/2789770.2789771) has implemented QJUMP as a Linux kernel module. It uses the traffic control subsystem. By using the CPU's timestamp counter[^29], the overhead is minimal - ~35 cycles per packet, or <0.5% of the total kernel processing path.

[Wang & Ng](https://dl.acm.org/doi/10.5555/1833515.1833691) used a tool called **Badabing** to measure Amazon EC2. While the average packet loss rate was very low[^30], loss episodes[^31] occurred in >10% of the intervals. Most of the time, the network isn't down in the sense of a broken cable; it's just congested.

In VoIP, if a packet is lost, there's no point in retransmitting it. **TCP** is designed for reliability. This is appropriate for bulk data transfer. If a packet is lost, TCP retransmits it, and the app doesn't see the data until the retransmission has arrived. This causes jitter. Modern data centers host a diverse range of apps. QJUMP allows latency-sensitive apps to exempt themselves from the interference of bulk traffic. QJUMP allows apps to sacrifice peak throughput.

[^01]: a packet
[^02]: due to a disconnected cable or faulty switch
[^03]: the network or recipient is overloaded
[^04]: due to a long garbage collection cycle
[^05]: one susceptible to indefinite communication disruptions
[^06]: a task handled by systems like Zookeeper
[^07]: often anecdotal
[^08]: misconfigured switches
[^09]: this is the idea behind **Chaos Monkey**
[^10]: typically 20 seconds
[^11]: like TCP or ZooKeeper haertbeats
[^12]: Saltzer JH, Reed, DP, & Clark, DD. (1984). *End-to-end arguments in system design.* ACM Transactions on Computer Systems, 2(4), 277–288. [https://doi.org/10.1145/357401.357402](https://groups.csail.mit.edu/ana/Publications/PubPDFs/End-to-End%20Arguments%20in%20System%20Design.pdf)
[^13]: a file checksum
[^14]: and to remove any ambiguity
[^15]: indicating **Host B** has closed
[^16]: the app
[^17]: TCP retries, ZooKeeper heartbeats
[^18]: the hose-constrained model
[^19]: where epochs occur at the same frequency but different phases
[^20]: steal time
[^21]: backpressure
[^22]: where *d* is max network delay and *r* is max node processing time
[^23]: cwnd
[^24]: switches
[^25]: worst-case E2E delay equation
[^26]: similar to standard Ethernet
[^27]: priorities 0-7
[^28]: high *f*
[^29]: rdtsc
[^30]: <0.5%
[^31]: 5ms slits where the path appears congested
