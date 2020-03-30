import collections
import itertools
import heapq


class Graph:

    def __init__(self, V=set(), E=collections.defaultdict(dict), matrix=[],
        directed=True
    ):
        if V:
            self.V = V
            self.E = E
        else:
            self.V = set(range(len(matrix)))
            self.E = {u: {v: matrix[u][v] for v in self.V} for u in self.V}
        if directed == False:
            for u in self.V:
                for v in self.V - set(self.E[u]):
                    self.E[u][v] = float('inf') * (u == v)
            for u, v in itertools.product(self.V, self.V):
                self.E[u][v] = self.E[v][u] = min(self.E[u][v], self.E[v][u])

    def dijkstra(self, source, trace=False):
        dist = {u: float('inf') for u in self.V}
        dist[source] = 0
        Q = [(d, u) for u, d in dist.items()]
        heapq.heapify(Q)
        if trace:
            paths = {u: [[u]] for u in self.V}
        while Q:
            d, u = heapq.heappop(Q)
            for v, weight in self.E[u].items():
                alt = d + weight
                if alt <= dist[v]:
                    if alt < dist[v]:
                        dist[v] = alt
                        heapq.heappush(Q, (alt, v))
                    if trace:
                        paths[v] = [x for x in paths[v] if x[0] == source
                        ] + [y + [v] for y in paths[u]]
        if trace:
            for u in paths:
                paths[u] = [x for x in paths[u] if x[0] == source]
        return paths if trace else dist

    def bellman_ford(self, source):
        dist = collections.defaultdict(lambda: float('inf'))
        dist[source] = 0
        predecessor = collections.defaultdict(None)
        for w, u in itertools.product(self.V, self.E):
            for v in self.E[u]:
                if dist[u] + self.E[u][v] < dist[v]:
                    dist[v] = dist[u] + self.E[u][v]
                    predecessor[v] = u
        return dist

    def floyd_warshall(self):
        dist = {u: collections.defaultdict(dict)}
        for u in self.V: dist[u][u] = 0
        for u in self.E:
            for v in self.E[u]:
                dist[u][v] = self.E[u][v]
        for v, u in itertools.product(self.E, self.E):
            if v in self.E[u]:
                for w in self.E[v]:
                    dist[u][w] = min(dist[u][w], dist[u][v] + dist[v][w])


def word_ladder(start, end, bank, trace=False):
    V = {start} | set(bank)
    neighbors = collections.defaultdict(set)
    for word in V:
        for i in range(len(word)):
            neighbors[word[:i] + '.' + word[i + 1:]].add(word)
    E = collections.defaultdict(dict)
    for wildcard in neighbors:
        for u, v in itertools.product(neighbors[wildcard],
        neighbors[wildcard]):
            if u != v:
                E[u][v] = 1
    d = Graph(V=V, E=E).dijkstra(start, trace)
    if end in d:
        return d[end]
    elif trace: return []
    else: return float('inf')