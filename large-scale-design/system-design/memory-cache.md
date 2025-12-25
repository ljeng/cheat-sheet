# Memory Cache

30 years of Moore's Law have antiquated the traditional disk-oriented DBMS buffer pool architecture. It's now feasible to store entire OLTP databases directly in RAM with main memory capacity growing from megabytes to hundreds of gigabytes - and soon terabytes - on commodity servers. The overwhelming majority of OLTP databases are less than 1 Tb in size and growing in size quite slowly. As such, I believe that OLTP should be considered a main-memory market. A new engine such as H-Store can achieve dramatically better performance. I'll broach two influential systems, H-Store and RAMCloud, examining their deft approaches to durability.

## In-memory Databases

An in-memory database stores its primary data entirely in main memory, using non-volatile storage for recovery rather than for runtime data access, achieving consummate performance gains by eliminating disk I/O latency from the query path.

Memcached is used purely as a volatile cache, but most in-memory databases embrace durability. Common strategies encompass

- *append-only logs*: writing a log of all changes to disk. The database can reload its state by replaying this log upon restart.
- **periodically** writing the entire in-memory state to disk.
- **replicating** the in-memory state to other machines so data survives a single-node failure
- *specialized hardware*: using battery-backed RAM ensures memory contents survive a power failure.

It's common to place an application-managed caching layer[^mc1] in front of a database. It is normally the application code's responsibility to keep the cache in sync with the main database in this model.

---

H-Store is a research database system designed from the ground up for high-throughput OLTP workloads. It operates on a shared-nothing cluster of nodes and is built on the principle that OLTP transactions are short-lived and are executed serially on a single CPU core to eliminate concurrency overhead.

Data is partitioned across a grid of computers. Each node is independent and manages its own data. Each CPU core on a node is treated as an independent, **single-threaded execution** site. This design eliminates unnecessary latching, creating a simpler codebase. H-Store assumes that applications interact with the database via pre-defined **stored procedures**. This minimizes network round-trips and allows for transaction analysis and optimization at definition time.

Many datasets fit in memory, but H-Store requires a  solution for cases where the database exceeds available RAM. This architecture is called **anti-caching**, as it's the inverse of a buffer pool. Anti-caching spills cold data from memory to disk instead of pulling hot data from disk into memory. A data tuple resides exclusively in one location in this model: either in main memory or on disk. It's never copied between the two. The DBMS monitors the amount of memory used. It "evicts” the least recently used (LRU) tuples to make space when the size of the database relative to the amount of available memory on the node exceeds some administrator-defined threshold.

### Eviction Process

The system maintains a separate LRU chain per table that is local to a partition. H-Store executes special single-partition transactions that select tuples for eviction. When the eviction transaction executes, it creates a new block by popping tuples off the head of the target table's LRU chain. For each tuple being evicted, H-Store copies its data into the eviction block buffer. It then adds an entry into the Evicted Table and updates all indexes to point to this entry instead of the original tuple location. Each tuple in the Evicted Table includes a special evicted flag in its header that enables the DBMS to recognize when a transaction accesses evicted data. Once the block is full, it's **written to disk** in a sequential write operation. The single-threaded nature of the execution engine means that no other transactions access these changes until the special transaction finishes.

### Retrieval Process

When a transaction attempts to access a tuple marked as evicted, the system intercepts the request. The transaction is switched into a **"pre-pass" mode**. It executes without making changes in this mode, simply to identify *all* the evicted data it needs. The transaction is **aborted**[^mc2] after the pre-pass. The system then issues an asynchronous request to **fetch** the required data blocks from disk in the background. The original transaction is **restarted** and executes to completion once the data is loaded back into the in-memory tables, this time with all its data in memory.

---

Nevertheless, maintaining the LRU ordering has a cost. Experiments show that a doubly-linked list is far more efficient than a singly-linked list for skewed workloads, as frequently accessed (hot) tuples near the tail of the list are updated quickly. The extra pointer's minor memory overhead is a worthwhile trade-off for the performance gain. The evicted block size impacts performance. Larger blocks reduce overall throughput, but they add the cost of being fetched. With a highly skewed workload, it is less common that multiple tuples from a single block will be requested together. Thus, the system is less likely to benefit from the locality of tuples on the same block.

## RAMCloud

RAMCloud is a low-latency key-value storage system. It sustains remote read/write times in the microsecond range by keeping all data in DRAM and using a log-structured partition for memory and disk management.

A RAMCloud cluster consists of master servers and backup servers. A master module manages the main memory of the server to store RAMCloud objects; it handles read and write requests from clients. A backup module uses local disk or flash memory to store backup copies of data owned by masters on other servers. The masters and backups are managed by a central coordinator that handles configuration-related issues such as cluster membership and the distribution of data among the servers. RAMCloud could use a master's memory as a log. New objects are simply appended at the end of the head segment. Each master's log is divided into 8 MB segments. Each segment is replicated to backups. This approach avoids allocation inefficiencies and unifies the information both in memory and on disk.

When an object is deleted or modified, RAMCloud does not modify the object's existing record in the log. Instead, it appends a tombstone record to the log. RAMCloud uses a log cleaner to reclaim free space that accumulates in the logs when objects are deleted or overwritten. The cleaner selects segments containing a high percentage of dead data, copies any live objects to new segments at the head of the log, and then frees the old segments. The cost of log cleaning rises rapidly as memory utilization increases. For example, the cleaner must copy 9 bytes of live data for every 1 byte of space it reclaims at 90% utilization, consuming bandwidth.

RAMCloud decouples memory cleaning from disk cleaning to manage this cost.

1. The first level of cleaning operates **only on the in-memory segments** on masters. It **compacts a segment**, copying its live data into a smaller region of memory and freeing the original storage.
1. The second level is the cleaning process that reclaims space on the backup disks. **Combined cleaning** is postponed by using segment compaction first to suppress the immediate need for garbage collection, allowing more time for objects to become obsolete, meaning segments will have lower utilization when they're finally cleaned, making the process much more efficient.

This two-level hierarchy leverages each medium's strengths: memory has plentiful bandwidth for compaction at high utilization, while disk has plentiful space to lower its effective utilization and reduce cleaning bandwidth requirements.

RAMCloud performs cleaning concurrently with normal read/write requests using multiple cleaner threads to hide its latency. This is simplified by the log-structured design. Segments are **immutable** once written, so cleaners can copy data without worrying about it being modified concurrently. All object lookups go through a central hash table. The cleaner can relocate an object and then **atomically update** the pointer in the hash table to refer to the new location. Fine-grained locking on hash table buckets is used to **manage contention** between cleaner and service threads. To prevent a cleaner from freeing a segment that a service thread is still reading, the system waits for all currently active RPCs to complete before reclaiming the segment's memory.

## Conclusion

The increasing affordability and capacity of RAM have catalyzed a paradigm shift in database architecture, moving from disk-centric models to in-memory designs optimized for low-latency workloads. **H-Store** postulates that it's possible to eliminate concurrency overheads through a stored-procedure-based model. Its **anti-caching** architecture embodies an elegant solution for managing datasets that exceed memory capacity by treating disk as a spill-over area for cold data, supplanting the buffer pools of the past. In parallel, **RAMCloud** invokes the power of a **log-structured memory** paradigm for key-value stores. This design introduces requisite garbage collection, but **two-level and parallel cleaning** suppress the overhead while maintaining high memory utilization and high-speed writes. These architectures renounce the "one size fits all" mentality in favor of specialized solutions that deliver dramatic performance improvements by girding their design around the realities of modern hardware.
