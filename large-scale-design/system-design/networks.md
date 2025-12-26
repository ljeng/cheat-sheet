# Networks

## Partitions in Systems

The distributed systems I advocate are **shared-nothing systems**: collections of machines connected by a network. The network is the sole communication channel; I assume each machine has its own disk, and one machine can't access another’s resources except by making requests over the network. This shared-nothing architecture is dominant for internet services because it's cost-effective using commoditized cloud infrastructure and achieves high reliability through redundancy. However, this reliance on the network introduces unreliability. The internet is an asynchronous **packet network**. A node can send a message[^1] to another in this model, but the network provides no guarantees about its delivery. Many things can go wrong when you send a request and expect a response. Your request packet may be lost in transit[^2]. Your request may be waiting in a queue and will be delivered later[^3]. The remote node may have crashed, been powered down, or become otherwise unavailable. The remote node may have paused[^4] but will resume responding later. The remote node may have processed your request, but **the response packet was lost** on its way back. The remote node may have processed the request, but **the response has been delayed** in transit.

Persistent network unreliability is so fundamental that it tops Peter Deutsch's list of "Eight Fallacies of Distributed Computing." This is unsurprising, as distributed programs' reliance on shared network channels defines them. Distributed computing revolves around the (im)possibilities of computation under varying network conditions.

For instance, consensus can't be guaranteed in an asynchronous network[^5] with even a single faulty process. The well-known FLP impossibility result demonstrates this. This isn't just a theoretical concern. These impossibility results have spurred system development. These impossibility proofs impose programmability limitations.

Some argue that networks are generally reliable. This would make extensive failure-mode design unnecessary. Others surmise differently. James Hamilton of AWS acknowledges that "Network partitions should be rare but net gear continues to cause more issues than it should." A question remains. What's the true state of network reliability?

Packet loss can be tracked. But the end-to-end impact on applications is far more elusive. Existing data is deployment-specific, vendor-dependent, and tied to particular topologies, making generalization difficult. Finally, distributed systems are inherently resilient. This means noticeable outages require complex interactions of multiple failure modes. Applications silently degrade under network stress. The underlying causes are obscure for extended periods.

Sysadmins share stories informally. But detailed network availability surveys are rare. Network problems are surprisingly common, even in controlled environments such as company-operated data centers. Anecdotal evidence suggests so. For example, one study in a medium-sized data center found approximately 12 network faults per month. Half disconnect a single machine and the other half disconnect an entire rack. Another study measured failure rates of load balancers. Redundant networking gear doesn't always palliate faults as much as expected against human error[^6], a major cause of outages.

Public clouds are notorious for transient network issues. Failures affect a specific availability zone or even create "planes of cleavage" in the underlying hardware topology, where communication between certain subsections of a data center is impaired. Sometimes the hardware is fine but the software controlling it fails. Cloudflare deployed a new firewall rule to mitigate a DDoS attack in 2013. A bug in the Juniper routers' firmware caused them to consume all their memory and crash upon receiving this rule. The cascading failure brought down their network. Recovery proved arduous - engineers had to be physically dispatched to reboot routers, and the initial data centers that came back online were immediately overwhelmed by redirected traffic. The outage lasted for an hour. Failures over the WAN are also common and have a larger blast radius. They isolate entire data centers. The duration of 500 "isolating network partitions" varied from a median of 2.7 minutes for software-related failures to 32 minutes for hardware failures. The 95th percentile reached nearly four days for hardware issues. The Border Gateway Protocol (BGP) coordinates traffic across the global internet. Misconfigurations have catastrophic effects. Pakistan Telecom, attempting to block YouTube locally, accidentally advertised its block to the global internet in 2008. This hijacked traffic and made the site unreachable worldwide.

If software isn't designed to handle network faults, the consequences are severe. They range from service unavailability to catastrophic data loss.

> This was one of the worst outages in the history of GitHub, and it's not at all acceptable to us. I’m very sorry that it happened and our entire team is working hard to prevent similar problems in the future.

-- <cite>Mark Imbriaco, "Downtime Last Saturday"</cite>

If your network is usually stable, a valid approach is to simply show an error message to users. Rely on operators to fix the underlying issue. The system must be designed to recover gracefully once the network is restored, without deadlocking, corrupting data, or entering an unrecoverable state. The best practice is to test for these failures deliberately. Netflix's Chaos Monkey intentionally injects faults - including network partitions - into a production environment to test your system's response and corroborate that your system behaves as you designed it to when a real network fault occurs.

[^1]: a packet
[^2]: due to a disconnected cable or faulty switch
[^3]: the network or recipient is overloaded
[^4]: due to a long garbage collection cycle
[^5]: one susceptible to indefinite communication disruptions
[^6]: misconfigured switches
