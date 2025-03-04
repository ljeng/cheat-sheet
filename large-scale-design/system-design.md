# System Design

## Table of Contents

- [Feature Sets](#feature-sets)
- [Interfaces](#interfaces)
- [Class Hierarchies](#class-hierarchies)
- [Distributed Systems](#distributed-systems)
- [Designing a System Under Certain Constraints](#designing-a-system-under-certain-constraints)
- [Simplicity](#simplicity)
- [Limitations](#limitations)
- [Robustness](#robustness)
- [Tradeoffs](#tradeoffs)
- [How the Internet Works](#how-the-internet-works)
    - [Routers](#routers)
    - [Domain Name Servers](#domain-name-servers)
    - [Load Balancers](#load-balancers)
    - [Firewalls](#firewalls)
- [Traversing a Graph](#traversing-a-graph)
- [Run-time Complexity of Graphs](#run-time-complexity-of-graphs)
- [A Distributed Hash Table System](#a-distributed-hash-table-system)
- [Resource Estimation with Real Systems](#resource-estimation-with-real-systems)
- [The Big Product Design Picture](#the-big-product-design-picture)
- [Translation of an Abstract Problem to a System](#translation-of-an-abstract-problem-to-a-system)
- [API Discussions](#api-discussions)
- [Binary Trees](#binary-trees)
- [Cache](#cache)
- [MapReduce](#mapreduce)
- [For Loop Problems](#for-loop-problems)
- [Index](#index)
- [Reverse Linked List](#reverse-linked-list)
- [Compilers](#compilers)
- [Memory Cache](#memory-cache)
- [Networks](#networks)

## Feature Sets

## Interfaces

## Class Hierarchies

## Distributed Systems

## Designing a System Under Certain Constraints

## Simplicity

> Simplicity is a prerequisite for reliability.

-- <cite>Edsger W. Dijkstra</cite>

> Simplicity is the ultimate sophistication.

-- <cite>Leonardo da Vinci</cite>

We need to build simple systems if we want to design good software. There's not enough focus on simplicity. "Simple"[^simplicity01] means "one twist." "Complex" means "multiple twists" or "braided together." In software, this refers to whether it's folded together or not. People usually interchange "simple" with "easy." "Easy"[^simplicity02] means "near" or "familiar." All that's familiar is somewhat easy. Easiness is relative.

Simple things have one role, task, objective, or concept. They may be one dimension of a problem. They don't interleave issues. Simplicity doesn't mean one of a kind. An interface could have multiple methods and still be simple. Simplicity is objective.

Symptoms of complexity:

- explosion of the state space
- tight coupling
- tangled dependencies
- inconsistent naming
- special casing

[Moseley and Marks](https://curtclifton.net/papers/MoseleyMarks06a.pdf) look at which bits of complexity are accidental and which are essential. Essential complexity is inherent in the problem itself[^simplicity03]. It's the complexity that would exist even in an ideal development environment. Accidental complexity is complexity arising from implementation choices, suboptimal language and infrastructure, and performance issues. It's the complexity that could be avoided. Software engineering's goal should be to eliminate accidental complexity as much as possible and assist with essential complexity.

Avoid state and control where they aren't absolutely essential. Separate complexity that's either truly essential, or useful from a practical point of view from the rest of the system. Separate logic from state and essential complexity from accidental complexity. These principles aren't new.[^simplicity04]

Separate out the system's pure logic.

Essential state is the foundation. Changes to the essential state may require changes in other specifications, but changes in other specifications may never require changes to the essential state specification. Changes to the essential state may require changes to the logic, but changes to accidental state and control should never affect the essential logic. Accidental state and control are the least important conceptually. Changes here should never affect the other components.

A sharp focus on true essentials and avoiding useless complexity leads to less code. Good abstractions hide complexity. However, unneeded data abstraction can increase complexity due to subjectivity in grouping data. The relational model involves minimal commitment to subjective groupings, and this commitment has only minimal impact on the rest of the system.
Abstraction is a good tool for removing complexity. Good abstractions hide implementation details and behind a simple interface. For example, high-level programming languages hide machine code, and SQL hides data structures and concurrency.

- *What?* Define abstractions[simplicity05] as sets of functions. Make them small. Use polymorphism.
- *Who?* Define the data/entities your abstractions will use. Pass subcomponents as arguments. - Don't hardwire.
- *How?* Implement the details, using polymorphism and isolating implementations.
- *When?* Where? Avoid connecting objects directly; use queues to decouple them.
- *Why?* Use declarative systems to implement policies and rules. Rules tend to increase complex control flow.

Keep information simple. Don't use objects to handle information. Use generic constructs[^simplicity06] to manipulate information. Don't tie data logic to its representation. Avoid ORM where possible.

- *Values* - Use final, persistent collections.
- *Functions* - Use stateless methods.
- *Namespaces* - Use languages with good namespace support.
- *Data* - Use maps, arrays, sets, XML, JSON, etc.
- *Polymorphism* -  Use protocols, type classes.
- *Managed references* - Use Clojure, Haskell.
- *Set functions* - Use libraries.
- *Queues* - Use libraries.
- *Declarative data manipulation* - Use SQL, LINQ, Datalog.
- *Rules* - Use libraries or Prolog.

Choose simple tools. Write simple code. Simplify existing code by disentangling it.

Avoid tools[^simplicity07] that generate complex outputs. Reliability tools[^simplicity08] are good but secondary. They don't enforce simplicity; they're just a safety net. Simplify the problem before starting to code. Use abstractions and design upfront.

Isolate and gentrify a system's disordered parts. One frequently constructs a facade to put a "pretty face" in front of the unpleasant that's swept under the rug. Intention-revealing selectors expose functionality. Consolidation hems unregulated growth that may have occurred during prototyping or expansion.

Daily builds[^simplicity09] and keeping the last working version around are nearly universal practices among successful maintenance programmers. Rigorous testing[^simplicity10] is vital for ensuring a working system. Refactoring maintains order.

Functional programming (FP) has roots in the stateless lambda calculus, equivalent in computational power to the Turing machine. Whilst object-oriented programming was developed out of a desire to manage the stateful von Neumann architecture, FP avoids state-related complexity. This has very significant benefits for testing and reasoning.

[^simplicity01]: from "sim" and "plex"
[^simplicity02]: from the Latin for "adjacent"
[^simplicity03]: as seen by the users
[^simplicity04]: [Kowalski's "Algorithm = Logic + Control"](https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf) is a classic example.
[^simplicity05]: interfaces, protocols
[^simplicity06]: maps, etc.
[^simplicity07]: constructs
[^simplicity08]: testing, refactoring
[^simplicity09]: Microsoft, Nortel
[^simplicity10]: extreme programming's unit tests

## Limitations

## Robustness

## Tradeoffs

## How the Internet Works

### Routers

### Domain Name Servers

### Load Balancers

### Firewalls

## Traversing a Graph

The use of the same data value as a primary key and a secondary key is a basic concept. This reflects real-world relationships and re-establishes those relationships for processing. A programmer can:

1. start at the beginning or a known record and access records sequentially.
1. use a database key for direct access to a record's physical location.
1. use a primary data key.
1. use a secondary data key to access all records with that value.
1. traverse from a set's owner to its member records.
1. traverse between members of a set.
1. start from any member and access the owner of the set.

Data structure sets are declared and maintained. They contribute to programmers the capability to:

* associate records into sets.
* use these sets as retrieval paths.

```sql
CREATE TABLE vertices (
    vertex_id integer PRIMARY KEY,
    properties json);

CREATE TABLE edges (
    edge_id integer PRIMARY KEY,
    tail_vertex integer REFERENCES vertices (vertex_id),
    head_vertex integer REFERENCES vertices (vertex_id),
    label text,
    properties json);

CREATE INDEX edges_tails ON edges (tail_vertex);
CREATE INDEX edges_heads ON edges (head_vertex);

```

*Example TG-1*

For any vertex, you can retrieve both incoming and outgoing edges, thus traversing the graph forward and backward. That's why Example TG-1 has indexes on `tail_vertex` and `head_vertex`.

The directions of 'in' and 'out' were reversed. Where the input notion of the sequential file world meant 'into the computer from tape,' the new input notion became 'into the database.' This revolution in thinking changes the programmer from a stationary observer to a navigator traversing the database. Processing a single transaction involves a path through the database. A record would be used to gain access to other records. Each of these records is used in turn as a point for examining other sets. The [Neo4j Traversal API](https://neo4j.com/docs/) is a callback-based, lazily executed way for specifying these movements in Java. [Some traversal examples are collected.](https://neo4j.com/docs/2.0.0/tutorials-java-embedded-traversal.html) We want to train programmers to navigate in an *n*-dimensional data space. Neo4j's graph algorithms component contains implementations of common graph algorithms like:

- shortest paths
- all paths
- all simple paths
- Dijkstra's
- A*

This 'traverser' concept is new in TinkerPop3, providing the means by which steps remain stateless. A traverser maintains all the metadata about the traversal – how many times the traverser has gone through a loop, path history, the current object, etc. Path calculation is costly in terms of space. The traverser stores an array of previously visited objects. Thus, a traversal strategy analyzes whether path metadata is required. If not, path calculations are turned off. Never rely on the iteration order in TinkerPop3 traversals. Even within a release, traversal optimizations may alter the flow.

[Cypher](https://neo4j.com/docs/2.0.0/cypher-query-lang.html), a powerful declarative query language, queries the graph. [TinkerPop3's `GraphTraversal` JavaDoc](https://tinkerpop.apache.org/javadocs/3.4.6/core/org/apache/tinkerpop/gremlin/process/traversal/dsl/graph/GraphTraversal.html) lists all steps and their descriptions. The [Gremlin Console](https://tinkerpop.apache.org/docs/3.2.3/reference/#gremlin-console) can be used for these steps.

```groovy
gremlin> g.V // (1)
  ==>v[1]
  ==>v[2]
  ==>v[3]
  ==>v[4]
  ==>v[5]
  ==>v[6]

gremlin> g.V.name // (2)
  ==>marko
  ==>vadas
  ==>lop
  ==>josh
  ==>ripple
  ==>peter

gremlin> g.V.outE.weight // (3)
  ==>0.4
  ==>0.4
  ==>0.5
  ==>1.0
  ==>1.0
  ==>0.2

```

1. `g.V` retrieves all vertices. There's no need for parentheses.
1. `g.V.name` is interpreted as `g.V().values('name')`.
1. A chain of zero-argument step calls is followed by a property value call.

Domain-specific language authors should leverage the steps, as then the common optimization and decoration strategies can reason on the underlying traversal sequence. If new steps are introduced, these optimizations may not function properly.

Physics yields minimum-energy solutions; a similar science must be developed for database access. This includes the traversal of existing databases, building databases, and restructuring them to best fit the changing access patterns.

## Run-time Complexity of Graphs

## A Distributed Hash Table System

## Resource Estimation with Real Systems

## The Big Product Design Picture

## Translation of an Abstract Problem to a System

## API Discussion

## Binary Trees

## Cache

## MapReduce

### The Programming Model

MapReduce is a programming model and associated implementation designed for processing and generating large datasets that may not fit in the memory of a single machine. It simplifies distributed data processing by handling the complexities of parallelization, data distribution, fault tolerance, and load balancing. It allows programmers to utilize resources on large clusters of commodity machines without any experience in distributed systems. Users specify two functions, `map` and `reduce`.

A computation takes a set of input key-value pairs and produces a set of output key-value pairs. The user expresses the computation as two functions:

- **`map`**, written by the user, takes an input pair and produces intermediate key-value pairs. Think of this as transforming and extracting relevant data from each input record.
- The **`reduce`** function merges together all intermediate values associated with the same intermediate key, typically aggregating, summarizing, or filtering them, to produce zero one output values.

Programs written in this functional style are automatically parallelized and are fault-tolerant. Many real-world tasks, such as counting word occurrences in a large document collection, building inverted indexes, or analyzing web server logs, are expressible in this model. Although MapReduce's importance is declining, it provides a clear picture of why and how batch processing is useful. It was a major step forward in terms of the scale of processing that could be achieved on commodity hardware.

### Example: Word Count

```c++
map(String docName, String docContent):
  for each word w in docContent:
    EmitIntermediate(w, "1");

reduce(String word, Iterator values):
  int result = 0;
  for each v in values:
    result += ParseInt(v);
  Emit(AsString(result));

```

The `map` function emits each word plus a count of `1` in this example. The `reduce` function sums together all counts emitted for a particular word.

### Types

Even though the previous pseudocode is written in terms of string inputs and outputs, the `map` and `reduce` functions have associated types:

- `map (k1, v1) -> list(k2, v2)`
- `reduce (k2, list(v2)) -> list(v2)`

That is, the input keys and values `(k1, v1)` are drawn from a different domain than the output keys and values. The intermediate keys and values `(k2, v2)` are from the same domain as the output keys and values. The C++ implementation leaves it to the user code to convert between string and appropriate types.

### More Examples

* *Distributed Grep:* `map` emits a line if it matches a pattern; `reduce` is the identity function[^mr01].
* *Count of URL Access Frequency:* `map` outputs `<URL, 1>`; `reduce` adds the values for the same URL.
* *Reverse Web-Link Graph:* `map` outputs `<target, source>` for each link; `reduce` concatenates the list of source URLs associated with a target.
* *Term-Vector per Host:* `map` emits `<hostname, term_vector>`; `reduce` adds the term vectors together for a given host.
* *Inverted Index:* map emits `<word, documentID>`; `reduce` sorts corresponding document IDs and emits `<word, list(documentID)>`.
* *Distributed Sort:* `map` emits `<key, record>`; `reduce` emits all pairs unchanged[^mr02].

### Implementation and Execution

An implementation of MapReduce is targeted to large clusters of commodity PCs connected via switched Ethernet. in the environment:

1. Machines are typically dual-processor x86 machines with 2-4 GB of RAM running Linux.
1. Commodity hardware[^mr03] is used, averaging less overall bisection bandwidth.
1. A cluster contains hundreds or thousands of machines, and therefore failures are common.
1. Storage is provided by inexpensive IDE disks directly attached to machines, managed by a distributed file system that uses replication for fault tolerance.
1. Users submit jobs to a scheduling system that maps tasks to available machines.

### Execution Overview

```mermaid
flowchart TB
    A((User Program))
    B((Master))
    subgraph Input Files
        I0((split 0))
        I1((split 1))
        I2((split 2))
        I3((split 3))
        I4((split 4))
    end
    subgraph Map Phase
        W0((worker))
        W1((worker))
        W2((worker))
        W3((worker))
        W4((worker))
    end
    subgraph Intermediate Files
        IF((Intermediate files on local disks))
    end
    subgraph Reduce Phase
        R0((worker))
        R1((worker))
    end
    subgraph Output Files
        O0((output file 0))
        O1((output file 1))
    end
    A -- "(1) fork" --> A
    A -- "(1) fork" --> B
    B -- "(2) assign map" --> W0
    B -- "(2) assign map" --> W1
    B -- "(2) assign map" --> W2
    B -- "(2) assign map" --> W3
    B -- "(2) assign map" --> W4
    I0 -- "read" --> W0
    I1 -- "read" --> W1
    I2 -- "read" --> W2
    I3 -- "read" --> W3
    I4 -- "read" --> W4
    W0 -- "(4) local write" --> IF
    W1 -- "(4) local write" --> IF
    W2 -- "(4) local write" --> IF
    W3 -- "(4) local write" --> IF
    W4 -- "(4) local write" --> IF
    B -- "(3) assign reduce" --> R0
    B -- "(3) assign reduce" --> R1
    R0 -- "(5) remote read" --> IF
    R1 -- "(5) remote read" --> IF
    R0 -- "(6) write" --> O0
    R1 -- "(6) write" --> O1

```

*Figure MR-1*

The execution of a MapReduce operation proceeds as follows[^mr04]:

1. The input data[^mr05] is split into *M*[^mr06] independent chunks. This allows for parallel processing. It then starts multiple copies of the program on the cluster. One copy is the master, which assigns tasks to worker processes.
2. The library creates *M* `map` tasks and *R* `reduce` tasks. These tasks are assigned to worker machines in a cluster. A worker assigned a `map` task reads the corresponding input split, parses key-value pairs, and calls the user-defined `map` function for each pair. Intermediate key-value pairs are buffered in memory.
3. The master assigns idle workers either a `map` or a `reduce` task.
4. Periodically, buffered pairs are written to the worker's local disk, partitioned into *R* regions[^mr07]. The locations of these files are sent to the master.
5. When a `reduce` worker is notified by the master about the locations of intermediate files, it uses remote procedure calls to read the data from the `map` workers' local disks. After reading all its intermediate data, the `reduce` worker sorts it by the intermediate keys. If the data is too large for memory, an external sort is used.
6. Each `reduce` task receives an intermediate key and an iterator over the set of values associated with that key. The `reduce` worker iterates over the sorted intermediate data. The iterator allows processing of value lists that are too large to fit in memory. The user-defined `reduce` function is applied to produce the final output. For each unique key, it passes the key and the corresponding set of values to the user's `reduce` function. The output of the `reduce` function is appended to a final output file for that `reduce` partition. When all `map` and `reduce` tasks are complete, the master wakes up the user program. The output is available in *R* output files[^mr08]. These files are often used as input to another MapReduce job or another distributed application.

[^mr01]: simply passes the input through
[^mr02]: relying on MapReduce's partitioning and ordering
[^mr03]: 100 Mbits/s or 1Gbit/s at the machine level is used
[^mr04]: referring to the numbered steps in Figure MR-1
[^mr05]: often stored in file
[^mr06]: typically 16-64 MB each
[^mr07]: determined by a partitioning function, often `hash(key) mod R`
[^mr08]: once per reduce task

## For Loop Problems

## Index

## Reverse Linked List

## Compilers

## Memory Cache

## Networks
