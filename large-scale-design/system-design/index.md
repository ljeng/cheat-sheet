# Index

## Indexing

Finding a specific piece of data in a database is slow if the system has to scan every row in a table. To solve this, we use an **index**: an additional data structure derived from the primary data that acts like a signpost locating the desired information. The trade-off in indexing is simple: **well-chosen indexes speed up read queries, but every index slows down writes.** This is because the index must also be updated each time data is written. Database admins must therefore choose which columns to index based on the app's typical query patterns to achieve the best performance balance.

## The B-tree: The Database Workhorse

The B-tree has been the essential, ubiquitous index structure in most database systems for decades. It organizes data in sorted order, allowing for efficient searches, insertions, deletions, and sequential access. A **primary index**[^01] defines the physical storage order of the table's data. A table can only have one primary index since the data itself is the index. A **secondary index**[^02] is a separate structure that contains the indexed column values and a pointer back to the corresponding row in the primary data structure. A table can have many secondary indexes. **Hash indexes** promise faster lookups for exact-match queries[^03], but **B-trees** have dominated. A B-tree's top levels[^04] are almost always cached in memory in practice. This means a search only requires a single disk I/O to fetch the leaf node, matching a hash index's **performance**. B-trees store keys in sorted order, making them highly efficient for **range queries**[^05]. Hash indexes are unordered and can't handle range queries. A B-tree on a multi-column key[^06] can **efficiently process queries on that key's prefix**[^07]. A hash index suffers from long "overflow chains” if many rows have the same key value, degrading performance. A B-tree **handles this gracefully** due to its balanced structure.

## Specialized Index Structures

B-trees are general-purpose, but specialized indexes exist for specific use cases.

Compression techniques make B-trees even more efficient. If all keys in a node share a common **prefix**[^08], that prefix is stored only once, saving space so more keys can fit in a node. It's unnecessary to use a child node's full key when devising a separator key for a branch node. The shortest possible key that correctly separates the two child ranges is used instead, further saving space.

A bitmap index is ideal for columns with a low number of distinct values[^09], common in data warehousing. For each unique value in the column, it creates a "bitmap" - a sequence of bits where each bit corresponds to a row in the table. A `1` indicates the row has that value, and a `0` indicates it doesn't. The bitmap's advantage is that logical queries[^10] are answered with extremely fast bitwise operations on these bitmaps before ever touching the table data.

Flash SSDs have different performance characteristics than conventional disks; random writes are particularly expensive. The **FD-Tree** (flash-friendly data tree) is designed with these principles in mind:

1. **Transform random writes into sequential ones.**
1. **Limit random writes to a small in-memory region.**

An FD-tree consists of a small in-memory B-tree[^11] and larger sorted runs on disk. New writes go only to the head tree. The head tree's contents are merged sequentially and in batches with the next level on disk when it's full. This design avoids costly random writes to the main data structure. To prevent long pauses during a large merge, a **de-amortization** technique is used, where the merge work is broken into small chunks and performed progressively alongside new insertions.

## Index Utilities

Managing indexes is a critical operational task that requires careful planning and execution, not simply creating them in an ad hoc manner and then just releasing them. The most efficient way to **create an index** on a large table isn't to insert one row at a time. The key values are instead extracted and then built into a balanced B-tree structure from the bottom up. This is orders of magnitude faster. **Deleting** large volumes of data is achieved by moving the records-to-be-deleted into a dedicated partition and then dropping that partition in a single fast operation. Insertions cause an index's pages to fragment on disk over time, slowing down scans. **Defragmentation** reorganizes the index pages to be physically contiguous, restoring optimal performance. Software faults can corrupt an index. **Verification** utilities scan the index structure, ensuring all invariants are correct. Advanced B-tree designs use **fence keys**[^12], making verification robust. **Dropping an index** is fast, as it simply updates database metadata and marks the space as free.

## Advanced Indexing

To optimize queries that frequently join tables[^13], a **merged index** physically co-locates related records from both tables within a single B-tree structure. All details for a given order are stored next to the order record itself by sorting records by a common key[^14]. This dramatically reduces the I/O required for joins while providing a viable solution that captures denormalization's performance benefits without altering the logical database schema.

A B-tree's flexibility inspires creativity. For example, one can create a B-tree on the keys' *hash values*. This concatenates a B-tree's ordered traversal and range-scan benefits with the uniform key distribution that a hash function implies, creating a powerful hybrid architecture that serves as a fulcrum for balanced query performance while avoiding the overhead of redundant data structures.

[^01]: also called a *clustered index* or *index-organized table*
[^02]: or *non-clustered index*
[^03]: often a single I/O operation
[^04]: branch nodes
[^05]: `WHERE price BETWEEN 100 AND 200`
[^06]: `lastname`, `firstname`
[^07]: searching by just `lastname`
[^08]: "Smith, J"
[^09]: low cardinality
[^10]: `AND`, `OR`, `NOT`
[^11]: the *head tree*
[^12]: copies of separator keys stored in child nodes
[^13]: `Orders` and `Order_Details`
