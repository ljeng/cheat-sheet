### Minimum Spanning Tree
```python
class SpanningForest:

    def __init__(self, trees, edges):
        # type vertices = iterable, type edges = adjacency dict
        self.trees, self.edges = trees, edges

    def kruskals(self):
        forest = [{u} for u in self.trees]
        index_map = {list(forest[i])[0]: i for i in range(len(forest))}
        adjacency_list = [(u, v, self.edges[u][v]) for u in self.edges for v in self.edges[u]]
        adjacency_list.sort(key = lambda x: x[2])
        mst = {u: dict() for u in self.trees}
        for u, v, weight in adjacency_list:
            if index_map[u] != index_map[v]:
                u, v = sorted([u, v], key = lambda x: len(forest[index_map[x]]))
                for w in list(forest[index_map[u]]):
                    forest[index_map[u]].remove(w)
                    forest[index_map[v]].add(w)
                    index_map[w], mst[u][v] = index_map[v], weight
        # output type: adjacency dict
        return mst
```