# Run-time Complexity of Graphs

We adopt the Turing machine (TM) model to analyze query complexity. Difficulty is measured by the resources required - usually **time** and **space** - relative to the input size $\|w\|$.

- *PTIME*[^01]: Problems solvable in polynomial time. This is the standard benchmark for tractability.
- *LOGSPACE*: Problems solvable using work tape space logarithmic to the input size. The input is kept on a read-only tape since the input itself is larger than the work tape.
- *PSPACE*[^02]: Problems solvable in polynomial space. $PSPACE = NPSPACE$ by Savich's theorem.

$$\text{LOGSPACE} \subseteq \text{PTIME} \subseteq \text{NP} \subseteq \text{PSPACE} \subset \text{TIME}(\text{Hyp})$$

A language $K$ is **complete** in $C$ if solving it allows solving all other problems in $C$, also within $C$. Therefore, the definition of completeness in a class $C$ requires the complexity of the reduction function to be lower than that for $C$.

| Type of Completeness | Type of Reduction |
| -------- | ---------------- |
| P-completeness    | LOGSPACE reductions |
| NP-completeness   | PTIME reductions   |
| PSPACE-completeness | PTIME reductions  |

The two main possible ways to look at the complexity of queries are as follows:

1. *Data complexity*: the complexity of evaluating a *fixed* query for variable database inputs
1. *Expression complexity*: the complexity of evaluating, on a *fixed* database instance, the various queries specifiable in a given query language

The usual situation is that the size of the database inputs dominates by far the size of the query, so data complexity is typically most relevant.

Complexity is formally defined via the **recognition problem**: Given an instance $I$ and a tuple $u$, is $u \in I$? We also measure the complexity of *constructing* the entire result since the recognition problem is the standard for complexity class categorization.

First-order logic queries[^03] are highly expressive.

- *LOGSPACE inclusion*: CALC queries are in QLOGSPACE. A TM can evaluate a query by using pointers[^04] to scan the input tape for each variable in the formula.
- *Parallel complexity*[^05]: CALC queries can be evaluated in **constant time** given a polynomial number of processors. This is because projection is mapped to constant-depth circuits.

Transitive closure and other recursive properties can't be expressed in CALC. This necessitates Datalog, which uses fixpoint evaluation. We use the semi-naïve algorithm to compute the result of a recursive Datalog program. The goal is to avoid redundant computations by only using newly derived tuples[^06] in each subsequent iteration. For a rule $p: −p_1 \ldots p_n, q_1 \ldots q_m$[^07], let $p\[i\]$ be the set of tuples at the start of iteration $i$, and let $\delta(p)\[i\]$ be the new tuples generated in iteration $i$. The update rule is

$$p[i + 1] = [i] \cup \Delta(p)[i]$$

## Delta Rules for Semi-naïve Evaluation

$$\Delta(p)[i]: -\delta(p_1)[i - 1], p[i - 1]_2...p[i - 1]_n, q_1...q_m$$

$$\Delta(p)[i]: -p[i]_1, \delta(p_2)[i - 1], p[i - 1]_3...p[i - 1]_n, q_1...q_m$$

$$\vdots$$

$$\Delta(p)[i]: -p[i]_1, p[i][n - 1], \delta(p_n)[i - 1], q_1...q_m$$

[^08]

---

Form the **precedence graph** $G_P$ as follows: Use the IDB predicates as the **nodes**. Include the **edge** $(R, R')$ if there's a rule with head predicate $R$ in which $R'$ occurs in the body. **Mutual recursion** is an equivalence relation on the IDB predicates of $P$, where each equivalence class corresponds to a strongly connected component[^09] of $G_P$.

The fact that each `fixpoint` query[^10] is in PTIME follows immediately from the inflationary[^11] nature of languages defining the `fixpoint` queries. The total number of tuples that can be built from constants in a given instance is polynomial in the size of the instance. The `while` queries with cumbersome updates are complete in PSPACE. A fundamental result is that `fixpoint` is complete in PTIME and that `while` is complete in PSPACE. These languages can't express simple queries[^12] if no order is provided.

We adopt a common notational convention for two parameters. Inside asymptotic notation, the symbol $V$ denotes $\|V\|$[^13] and the symbol $E$ denotes $\|E\|$[^14]. The function to compute the Bacon numbers evaluates every reachable node once and every edge twice, so it's $\Omega(V + E)$. In this graph, you'd expect that $E \gg V$, so this is reduced to $\Omega(E)$. To maintain $\Omega(1)$ performance, you need a constant time means of finding the node representing an actor such as a hash table mapping names to nodes. The name **"direct" algorithm** descends from the fact that the length of the computation doesn't depend on the length of paths in the underlying graph, very often making use of sparse matrices to represent them.

[^01]: TIME(Poly)
[^02]: SPACE(Poly)
[^03]: relational calculus or CALC
[^04]: logarithmic in size
[^05]: *AC<superscript>0</superscript>*
[^06]: deltas
[^07]: where *p<subscript>i</subscript>* are IDBs and *q<subscript>j</subscript> are EDBs
[^08]: and so on for all *n* IDB atoms
[^09]: cycle
[^10]: Datalog
[^11]: tuples are never removed
[^12]: like checking if the number of elements is even
[^13]: number of vertices
[^14]: number of edges
