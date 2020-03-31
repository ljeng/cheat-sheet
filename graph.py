import collections
import itertools
import heapq


class Graph:

    def __init__(self, V, E, directed=True):
        self.V = V
        self.E = E
        if directed == False:
            for u in self.V:
                for v in self.V - set(self.E[u]):
                    self.E[u][v] = float('inf') * (u != v)
            for u, v in itertools.permutations(self.V, 2):
                self.E[u][v] = self.E[v][u] = min(self.E[u][v], self.E[v][u])

    def count_components(self):
        V = collections.OrderedDict({u: None for u in self.V})
        counter = 0
        while V:
            stack = [V.popitem()[0]]
            while stack:
                u = stack.pop()
                for v in self.E[u]:
                    if self.E[u][v] < float('inf') and v in V:
                        stack += [v]
                        del V[v]
            counter += 1
        return counter

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
        dist = {u: {v: float('inf') for v in self.V} for u in self.V}
        for u in self.V:
            dist[u][u] = 0
        for u in self.E:
            for v in self.E[u]:
                dist[u][v] = min(dist[u][v], self.E[u][v])
        for w, u, v in itertools.permutations(self.V, 3):
            dist[u][v] = min(dist[u][v], dist[u][w] + dist[w][v])
        return dist

r3 = lambda k: range(k - 1, k + 2)

def get_neighbors(matrix, i, j, node=1, directional=4):
    if directional == 4:
        neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
    elif directional == 8:
        neighbors = set(itertools.product(r3(i), r3(j))) - {(i, j)}
    return [(row, col) for row, col in neighbors if 0 <= row < len(matrix) and
        0 <= col < len(matrix[0]) and matrix[row][col] == node
    ]

def to_graph(matrix, node=1, directional=4):
    if matrix:
        r = lambda x: range(len(x))
        n, m = len(matrix), len(matrix[0])
        V = {(i, j) for i, j in itertools.product(r(matrix), r(matrix[0]))
        if matrix[i][j] == node}
        E = collections.defaultdict(dict)
        for i, j in V:
            for row, col in get_neighbors(matrix, i, j, node, directional):
                E[(i, j)][(row, col)] = 1
        return Graph(V, E)
    return Graph(set(), collections.defaultdict(dict))


def word_ladder(start, end, bank, trace=False):
    V = {start} | set(bank)
    neighbors = collections.defaultdict(set)
    for word in V:
        for i in range(len(word)):
            neighbors[word[:i] + '.' + word[i + 1:]].add(word)
    E = collections.defaultdict(dict)
    for wildcard in neighbors:
        for u, v in itertools.permutations(neighbors[wildcard], 2):
            if u != v:
                E[u][v] = 1
    dist = Graph(V, E).dijkstra(start, trace)
    if end in dist:
        return dist[end]
    elif trace:
        return []
    else:
        return float('inf')