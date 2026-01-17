# Traversing a Graph

*Input* and *output* were defined by the movement of data from tape into the computer's memory in the era of sequential file processing. That has been reversed today: input now means *into the database*. This revolution in thinking transforms the programmer from a stationary viewer - watching objects pass through the CPU core as a passive observer - into a **mobile navigator**. Modern programmers are empowered to probe a multi-dimensional data space at will, starting from any known record and following relationships to discover insights.

Modern framework architecture eschews archaic patterns, and **TinkerPop3** introduces the **traverser** to facilitate this navigation. This is the engine that orchestrates steps within a query, yet remains stateless. A traverser garners all necessary metadata about its journey, including the current object being processed, the path history[^1], and loop counts[^2]. Path calculation is memory-intensive. An array of previously seen objects is stored in each path of the respective traverser. Traversal strategies automatically analyze queries to determine if path metadata is required; if not, these calculations are disabled to save space. Never rely on a specific iteration order between TinkerPop3 releases - or even within a single release - as traversal optimizations alter the underlying data flow.

The navigator mindset is conceptual, and the underlying storage must support movement. A property graph is modeled to facilitate bidirectional traversal even within a relational[^3] schema.

```sql
CREATE TABLE vertices (vertex_id integer PRIMARY KEY, 
    properties json);
CREATE TABLE edges (edge_id integer PRIMARY KEY,
    tail_vertex integer REFERENCES vertices (vertex_id),
    head_vertex integer REFERENCES vertices (vertex_id),
    label text,
    properties json);
CREATE INDEX edges_tails ON edges (tail_vertex);
CREATE INDEX edges_heads ON edges (head_vertex);

```
 
A programmer finds incoming and outgoing edges by indexing the `tail_vertex` and `head_vertex` like a novice navigating by crude landmarks, whereas the navigator follows a path through a chain of vertices forward and backward.

A full-fledged navigator utilizes convenient entry points into the graph.

1. *Direct access*: entering the database via a database key[^4]
1. *Primary key entry*: accessing data via indexed randomized access techniques
1. *Secondary key entry*: accessing all records sharing a data value
1. *Set navigation*: moving from an owner record to all member records[^5]
1. *Directional movement*: moving to the next member within a set or moving from a member back to its owner

This ability transmutes records into data structure sets that beckon the programmer to use these sets as retrieval paths, turning a single transaction into a sophisticated journey through the data.

Modern graph databases proffer high-level APIs to execute these navigations without manual pointer management. Neo4j tenders a dedicated **Traversal API**[^6] and the Cypher Query Language, a declarative way to query graphs. It also encompasses a library of graph algorithms for navigation, including shortest path / all path, Dijkstra, and all simple paths. Traversals are composed of chains of steps in Gremlin. Gremlin employs shorthand syntax for ease of use where parentheses are omitted for zero-argument method calls.

```groovy
gremlin> g.V 
  ==>v[1]
  ==>v[2]
gremlin> g.V.name 
  ==>marko
  ==>vadas
gremlin> g.V.outE.weight 
  ==>0.4
  ==>0.5

```

It's vital to hew to provided standard steps when building domain-specific languages, lest practitioners inadvertently obviate common decoration strategies that correctly reason on the traversal sequence.

We must develop a minimum-energy science for database access as we move forward - a paradigm intrinsic not just to the mechanics of traversing an existing database, but to the architecture of building databases to fit ever-changing access patterns. The goal remains the same: to equip the navigator with the most efficient path through an *n*-dimensional data space.

[^1]: the sequence of steps taken
[^2]: how many times a cycle has been executed
[^3]: SQL
[^4]: a permanent virtual memory address assigned at record creation
[^5]: converting a primary key into a secondary key
[^6]: a callback-based, lazily-executed Java API
