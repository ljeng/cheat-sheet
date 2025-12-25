# Run-time Complexity of Graphs

When we characterize the running time of a graph algorithm on a given graph $G = (V, E)$, we usually measure the size of the input in terms of the number of vertices $\vert V \vert$ and the number of edges $\vert E \vert$ of the graph. That is, we describe the size of the input with two parameters, not just one. We adopt a common notational convention for these parameters. Inside asymptotic notation[^1] and only inside such notation, the symbol $V$ denotes $\vert V \vert$ and the symbol $E$ denotes $\vert E \vert$. For example, we might say, "the algorithm runs in time $O(VE)$," meaning that the algorithm runs in time $O(\vert V \vert \vert E \vert)$. This convention makes the running-time formulas easier to read without risk of ambiguity.

[^1]: such as *O*-notation or *Θ*-notation
