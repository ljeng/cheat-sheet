# Cache

I discuss caching in database performance in optimizations to the [Shore database system](https://research.cs.wisc.edu/shore/) and their benefits of cache-conscious data structures.

I clarify a common misconception about in-memory databases. Counterintuitively, the performance advantage of in-memory databases isn't due to the fact that they don't need to read from disk. Modern operating systems cache recently used disk blocks in memory. Therefore, even a disk-based storage engine may never need to read from disk if you have enough memory if sufficient RAM is available. They can be faster because they can avoid the overheads of encoding in-memory data structures in a form that can be written to disk.

Optimizations to Shore reduced overhead in areas like concurrency control and recovery[^1]. Optimizations remove 80-88% of the time spent in B-tree operations without changing the key access pattern. Switching from a stripped-down Shore to a minimal-overhead kernel removes three-quarters of the remaining time. Optimizing components other than data structures themselves[^2] has a more substantial initial impact on performance than solely cache-optimized data structures.

"Cache-conscious" data structures minimize cache misses. A cache miss occurs when the CPU needs data that isn't currently in the fast cache memory[^3], forcing it to retrieve the data from slower main memory[^4] or, even worse, from disk. While efficient for disk-based systems, traditional B-trees aren't inherently cache-conscious. They can lead to cache misses as the CPU traverses the tree, accessing nodes not contiguous in memory. Cache-conscious research on B-trees improves data locality and targets cache misses. This rearranges the B-tree node layout in memory to increase the likelihood that related nodes are stored close together, improving the chances that they'll be loaded into the cache together.

While initial optimizations focused on higher-level system components, once a system is stripped down to a very basic kernel, cache misses in the B-tree code may well be the new bottleneck. At this point, it may be the case that other indexing structures, such as hash tables, perform better in this new environment. For example, hash tables offer better performance characteristics in a highly optimized, in-memory environment. However, these conjectures should be carefully tested.

[^1]: ensuring consistency after failures
[^2]: concurrency control, recovery
[^3]: L1, L2, L3 caches
[^4]: RAM
