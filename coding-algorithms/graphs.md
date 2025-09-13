# Graphs

## Table of Contents

- [Algorithms](#algorithms)
    - [Distance](#distance)
    - [Search](#search)
    - [Connectivity](#connectivity)
    - [Cycle Detection](#cycle-detection)
- [Ways to Represent a Graph in Memory](#ways-to-represent-a-graph-in-memory)
    - [Objects and Pointers](#objects-and-pointers)
    - [Matrix](#matrix)
    - [Adjacency List](#adjacency-list)
- [Traversal Algorithms](#traversal-algorithms)
    - [Breadth-first Search](#breadth-first-search)
    - [Depth-first Search](#depth-first-search)

### [class graph.**Graph**(*V*, *E*, *directed=True*)](code/graph.py)

A `Graph` is a mathematical structure defined by a set of vertices `V` connected by edges `E`, where the distance from vertex `u` to vertex `v` is `E[u][v]`. A `Graph` can be `directed` or undirected. `Graph` objects support the following methods:

## Algorithms

### Distance

**dijkstra**(*source*, *trace=False*)

Apply Dijkstra's algorithm. Return a dictionary in the form of `{u: distance}` where there is some `distance` from vertex `source` to vertex `u`. If `trace` is `True`, instead return a dictionary in the form of `{u: [[source...u]]}` where each list in the value is a path from `source` to `u`.

#### Shortest Path in Binary Matrix

Given an `n * n` binary matrix grid, return the length of the shortest **clear path** in the matrix. If there is no clear path, return `-1`. A **clear path** in a binary matrix is a path from the **top-left** cell[^1] to the bottom-right cell[^2] such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected[^3].
- The **length of a clear path** is the number of visited cells of this path.

```python
import itertools
import numpy as np
import scipy.sparse as sparse

toInt = lambda x: int(x.real) * n + int(x.imag)

directions = [dx + dy*1j
    for dx, dy
    in itertools.product(range(-1, 2), repeat=2)
    if not dx == dy == 0]

def shortestPathBinaryMatrix(grid):
    if grid[0][0] or grid[-1][-1]: return -1
    n = len(grid)
    k, m = n - 1, pow(n, 2)
    cells = np.fromfunction(lambda i, j: i + 1j*j, (n, n))
    chebyshev = np.maximum(k - cells.real, k - cells.imag).ravel()
    source, destination = [], []
    d_chebyshev = []
    for ui, uj in itertools.product(range(n), repeat=2):
        if grid[ui][uj]: continue
        u_int = toInt(ui + uj*1j)
        for d in self.directions:
            v_complex = ui + uj*1j + d
            vi, vj = int(v_complex.real), int(v_complex.imag)
            if 0 <= vi < n and 0 <= vj < n and not grid[vi][vj]:
                source.append(u_int)
                v_int = toInt(v_complex)
                destination.append(v_int)
                d_chebyshev.append(chebyshev[v_int] - chebyshev[u_int] + 1)
    chebyshev[0] += sparse.csgraph.dijkstra(csgraph=sparse
        .csr_matrix((d_chebyshev, (source, destination)),  shape=(m, m)),
            indices=0)[m - 1]
    return -1 if np.isinf(chebyshev[0]) else int(chebyshev[0]) + 1

```

#### Network Delay Time

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u[i], v[i], w[i])`, where `u[i]` is the source node, `v[i]` is the target node, and `w[i]` is the time it takes for a signal to travel from source to target. We will send a signal from a given node `k`. Return the *minimum* time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

```python
import numpy as np
from scipy import sparse

def networkDelayTime(times, n, k):
    source, target, time = [], [], []
    for u, v, w in times:
        source.append(u - 1)
        target.append(v - 1)
        time.append(w)
    min_time = sparse.csgraph.dijkstra(sparse
            .csr_matrix((time, (source, target)), shape = (n, n)),
        indices = k - 1)
    return -1 if np.isinf(min_time).any() else int(np.max(min_time))

```

[Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders)
```python
import collections


def snakesAndLadders(board):
    arr = []
    while board:
        arr += board.pop()
        if board: arr += board.pop()[::-1]
    m = len(arr)
    V = set(range(m))
    E = collections.defaultdict(dict)
    for u in V:
        for i in range(1, 7):
            v = u + i
            if v < m:
                if arr[v] == -1:
                    E[u][v] = 1
                else: E[u][arr[v] - 1] = 1
    moves = Graph(V, E).dijkstra(0)[m - 1]
    return moves if moves < float('inf') else -1
```

[Shortest Path Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix)
```python
def shortestPathBinaryMatrix(grid):
    dist = to_graph(grid, color=0, k=8).dijkstra((0, 0))
    m = len(grid) - 1
    k = m, m
    return dist[k] + 1 if k in dist and dist[k] < float('inf') else -1
```

[Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors)
```python
import collections


def shortestAlternatingPaths(n, red_edges, blue_edges):
    r = range(n)
    V = set()
    for X in r:
        V.add((X, 'red'))
        V.add((X, 'blue'))
    E = collections.defaultdict(dict)
    for u, v in red_edges:
        E[(u, 'red')][(v, 'blue')] = 1
    for u, v in blue_edges:
        E[(u, 'blue')][(v, 'red')] = 1
    graph = Graph(V, E)
    start_red, start_blue = graph.dijkstra((0, 'red')), graph.dijkstra((0, 'blue'))
    answer = []
    for X in r:
        u, v = (X, 'red'), (X, 'blue')
        length = min(start_red[u], start_red[v], start_blue[u], start_blue[v])
        answer += [length if length < float('inf') else -1]
    return answer
```

[Jump Game III](https://leetcode.com/problems/jump-game-iii)
```python
import collections


def canReach(arr, start):
    E = collections.defaultdict(dict)
    for i, x in enumerate(arr):
        j = i + x
        if j < len(arr):
            E[i][j] = 1
        j = i - x
        if 0 <= j:
            E[i][j] = 1
    dist = Graph(set(range(len(arr))), E).dijkstra(start)
    return any(dist[i] < float('inf') and x == 0 for i, x in enumerate(arr))
```

[Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees)
```python
import collections


def numOfMinutes(n, headID, manager, informTime):
    E = collections.defaultdict(dict)
    for i, x in enumerate(manager):
        E[x][i] = float('inf')
    for employee in V:
        for subordinate in E[employee]:
            E[employee][subordinate] = informTime[employee]
    return max(Graph(set(range(n)), E).dijkstra(headID).values())
```

**bellman_ford**(*source*)

Apply the Bellman-Ford algorithm. Return a `collections.defaultdict(dict)` object in the form of `defaultdict(<class 'dict'>, {u: distance})` where there is some `distance` from vertex `source` to vertex `u`.

**floyd_warshall**()

Apply the Floyd-Warshall algorithm. Return a dictionary in the form of `{u: {v: distance}}` where there is some `distance` from vertex `u` to vertex `v`.

[Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/contest/weekly-contest-173/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance)
```python
import collections


def findTheCity(n, edges, distanceThreshold):
    V = set(range(n))
    E = collections.defaultdict(dict)
    for from_, to_, weight in edges:
        E[from_][to_] = weight
    dist = Graph(V, E, directed=False).floyd_warshall()
    return min(V, key = lambda y: (sum(map(
        lambda x: x <= distanceThreshold, dist[y].values()
    )), -y))
```

### Search

### Connectivity

**count_components**()

Return the number of connected components.

#### Number of Islands
```python
def numIslands(grid):
    return to_graph(grid, color='1').count_components()
```

You are given an empty 2-D binary grid `grid` of size `m * n`. The grid represents a map where `0`'s represent water and `1`'s represent land. Initially, all the cells of `grid` are water cells[^4]. We may perform an add land operation which turns the water at position into a land. You are given an array `positions` where `positions[i] = [r[i], c[i]]` is the position `(r[i], c[i])` at which we should operate the `i`th operation. Return an array of integers `answer` where `answer[i]` is the number of islands after turning the cell `(r[i], c[i])` into a land. An *island* is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```python
def find(self, x):
    root = x
    while cell_root[root] != root: root = cell_root[root]
    while x != root:
        parent, cell_root[x] = cell_root[x], root
        x = parent
    return root

def numIslands2(m, n, positions)
    cell_root = dict()
    islands = 0
    answer = []
    for r, c in positions:
        u = r + c * 1j
        if u in cell_root:
            answer.append(islands)
            continue
        cell_root[u] = u
        islands += 1
        for d in [-1, -1j, 1j, 1]:
            v = u + d
            if v in cell_root:
                u_root, v_root = find(u), find(v)
                if u_root != v_root:
                    cell_root[u_root] = v_root
                    islands -= 1
        answer.append(islands)
    return answer

```

[Friend Circles](https://leetcode.com/problems/friend-circles)
```python
import collections
import itertools


def findCircleNum(M):
    V = set(range(len(M)))
    E = collections.defaultdict(dict)
    for i, j in itertools.permutations(V, 2):
        if M[i][j]:
            E[i][j] = 1
    return Graph(V, E, directed=False).count_components()
```

**kruskal**()

Apply Kruskal's algorithm to an undirected graph. Return a minimum spanning tree `MST` in the form of a `collections.defaultdict(dict)` object, where the distance from vertex `u` to vertex `v` is `MST[u][v]`.

**prim**()

Apply Prim's algorithm to an undirected graph. Return a minimum spanning tree MST in the form of a collections.defaultdict(dict) object MST.

[Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
```python
import collections

def findCheapestPrice(n, flights):
    E = collections.defaultdict(dict)
    for u, v, w in flights:
        E[u][v] = w
    ordering = Graph(set(range(n)), E, False).prim()
    return sum(ordering.values())
```

### Cycle Detection

**bipartite**()

Return whether the graph is bipartite.

[Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite)
```python
import collections


def isBipartite(graph):
    E = collections.defaultdict(dict)
    for u, x in enumerate(graph):
        for v in x:
            E[u][v] = 1
    return Graph(set(range(len(graph))), E, directed=False).bipartite()
```

[Possible Bipartition](https://leetcode.com/problems/possible-bipartition)
```python
import collections


def possibleBipartition(N, dislikes):
    E = collections.defaultdict(dict)
    for u, v in dislikes:
        E[u][v] = 1
    return Graph(set(range(1, N + 1)), E, directed=False).bipartite()
```

#### Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you. You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are *sorted lexicographically*[^5] by the rules of this new language. If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`. Otherwise, return a string of the unique letters in the new alien language sorted in *lexicographically increasing order* by the new language's rules. If there are multiple solutions, return *any of them*.

```python
import itertools
import graphlib

def alienOrder(words):
    graph = {letter: set() for word in words for letter in word}
    for word1, word2 in itertools.pairwise(words):
        for letter1, letter2 in itertools.zip_longest(word1, word2):
            if letter1 != letter2:
                if letter2 is None: return ''
                else:
                    if letter1 is not None: graph[letter2].add(letter1)
                    break
    try: return ''.join(graphlib.TopologicalSorter(graph).static_order())
    except graphlib.CycleError: return ''

```

## Ways to Represent a Graph in Memory

### Objects and Pointers

### Matrix

#### [graph.**to_graph**(*matrix*, *color=1*, *k=4*)](code/graph.py)

Convert a `matrix` to a `Graph`. Each node is marked `color` and are `k`-directionally connected to its neighbors, where `k` can be 4 or 8.

### Adjacency List

#### [graph.**get_neighbors**(*matrix*, *i*, *j*, *color=None*, *k=4*)](code/graph.py)]

In a `matrix`, nodes are marked `color` and are `k`-directionally connected to their neighbors, where `k` can be 4 or 8. Given a node at `(i, j)`, return its neighbors.

[Minesweeper](https://leetcode.com/problems/minesweeper)
```python
def updateBoard(board, click):
    i, j = click
    if board[i][j] == 'M':
        board[i][j] = 'X'
    elif board[i][j] == 'E':
        stack = [(i, j)]
        visited = set()
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            m = len(get_neighbors(board, i, j, color='M', k=8))
            if m:
                board[i][j] = str(m)
            else:
                board[i][j] = 'B'
                for u in get_neighbors(board, i, j, color='E', k=8):
                    if u not in visited:
                        stack += [u]
    return board
```

## Traversal Algorithms

### Breadth-first Search

#### Word Ladder

A *transformation sequence* from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s[1] -> s[2] -> ... -> s[k]` such that:

- Every adjacent pair of words differs by a single letter.
- Every s[i] for `1 <= i <= k` is in `wordList`. `beginWord` does not need to be in `wordList`.
- `s[k] == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the **number of words** in the **shortest transformation sequence** from `beginWord` to `endWord`, or `0` if no such sequence exists.

```python
import itertools

class Tree:
    def __init__(self, index):
        self.nodes, self.leaves = {index}, {index}

    def intersect(self, other):
        return self.nodes & other.nodes

    def expand(self, adjacency, other):
        self.leaves = set(itertools.chain(*(adjacency[i]
            for i in self.leaves))) - self.nodes
        self.nodes.update(self.leaves)
        return not self.leaves or self.intersect(other)

def ladderLength(beginWord, endWord, wordList):
    indexBegin = indexEnd = -1
    for i, word in enumerate(wordList):
        if word == beginWord: indexBegin = i
        elif word == endWord: indexEnd = i
    if indexBegin == -1:
        indexBegin = len(wordList)
        wordList.append(beginWord)
    if indexEnd == -1: return 0
    n, m = len(wordList), len(beginWord)
    adjacency = [set() for _ in range(n)]
    for i, word in enumerate(wordList):
        for j in range(i + 1, n):
            k = diff = 0
            while k < m: 
                diff += word[k] != wordList[j][k]
                if diff > 1: break
                k += 1
            else:
                adjacency[i].add(j)
                adjacency[j].add(i)
    begin, end = Tree(indexBegin), Tree(indexEnd)
    ladder_length = 2
    while True:
        if begin.expand(adjacency, end): break
        ladder_length += 1
        if end.expand(adjacency, begin): break
        ladder_length += 1
    return ladder_length if begin.intersect(end) else 0
    
```

Return *all the shortest transformation sequences* from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [`beginWord, s[1], s[2], ..., s[k]]`.

```python
from collections import defaultdict

class Tree:
    def __init__(self, index):
        self.root = index
        self.parent_children = defaultdict(set)
        self.child_parents = defaultdict(set)
        self.nodes, self.leaves = {index}, {index}

    def intersect(self, other):
        return self.nodes & other.nodes

    def expand(self, adjacency, other):
        parent_children = defaultdict(set)
        for i in self.leaves:
            for j in adjacency[i]:
                if j not in self.nodes: parent_children[i].add(j)
        self.leaves = set()
        for i, children in parent_children.items():
            self.parent_children[i].update(children)
            for j in children: self.child_parents[j].add(i)
            self.leaves.update(children)
        self.nodes.update(self.leaves)
        return not self.leaves or self.intersect(other)

    def prefixes(self, other):
        stack = [[j] for j in self.intersect(other)]
        prefixes = []
        while stack:
            current = stack.pop()
            if current[0] == self.root: prefixes.append(current)
            for i in self.child_parents[current[0]]:
                stack.append([i] + current)
        return prefixes

def findLadders(beginWord, endWord, wordList):
    indexBegin = indexEnd = -1
    for i, word in enumerate(wordList):
        if word == beginWord: indexBegin = i
        elif word == endWord: indexEnd = i
    if indexBegin == -1:
        indexBegin = len(wordList)
        wordList.append(beginWord)
    if indexEnd == -1: return []
    n, m = len(wordList), len(beginWord)
    adjacency = [set() for _ in range(n)]
    for i, word in enumerate(wordList):
        for j in range(i + 1, n):
            k = diff = 0
            while k < m: 
                diff += word[k] != wordList[j][k]
                if diff > 1: break
                k += 1
            else:
                adjacency[i].add(j)
                adjacency[j].add(i)
    begin, end = Tree(indexBegin), Tree(indexEnd)
    while True:
        if begin.expand(adjacency, end): break
        if end.expand(adjacency, begin): break
    ladders = set()
    for suffix in end.prefixes(begin):
        suffix.reverse()
        for prefix in begin.prefixes(end):
            for index, x in enumerate(suffix):
                if x == prefix[-1]:
                    ladders.add(tuple(prefix + suffix[index + 1:]))
                    break
    return [[wordList[i] for i in ladder] for ladder in ladders]

```

[Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation)
```python
def minMutation(start, end, bank):
    mutations = word_ladder(start, end, bank)
    return mutations if mutations < float('inf') else -1
```

#### Bus Routes

You are given an array `routes` representing bus `routes` where `routes[i]` is a bus route that the `i`<super>th</super> bus repeats forever.

- For example, if `routes[0] = [1, 5, 7]`, this means that the `0`<super>th</super> bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

You will start at the bus stop `source`[^6], and you want to go to the bus stop `target`. You can travel between bus stops by buses only. Return the least number of buses you must take to travel from `source `to `target`. Return `-1` if it is not possible.

```python
import collections

def numBusesToDestination(routes, source, target):
    graph = collections.defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
           graph[stop].add(i)
    queue = collections.deque([(source, 0)])
    traveled_routes = set()
    traveled_stops = {source}
    while queue:
        stop, buses = queue.popleft()
        if stop == target: return buses
        for i in graph[stop]:
            if i in traveled_routes: continue
            traveled_routes.add(i)
            for j in routes[i]:
                if j not in traveled_stops:
                    traveled_stops.add(j)
                    queue.append((j, buses + 1))
    return -1

```

### Depth-first Search

**toposort**()

Return a topological sort of the graph. If the graph has cycles, return `None`.

[Course Schedule](https://leetcode.com/problems/course-schedule)
```python
import collections


def canFinish(numCourses, prerequisites):
    E = collections.defaultdict(dict)
    for v, u in prerequisites:
        E[u][v] = 1
    return Graph(set(range(numCourses)), E).toposort() != None
```

[Course Schedule II](https://leetcode.com/problems/course-schedule-ii)
```python
import collections


def findOrder(numCourses, prerequisites):
    E = collections.defaultdict(dict)
    for v, u in prerequisites:
        E[u][v] = 1
    ordering = Graph(set(range(numCourses)), E).toposort()
    return ordering if ordering != None else []
```

#### [graph.**flood_fill**(*matrix*, *i*, *j*, *color*, *k=4*)](code/graph.py)

Flood fill a `matrix` in-place at coordinate `(i, j)` with `color`. Update `(i, j)` with `color`. Recursively update all `k`-directionally connected neighbors of `(i, j)` of the original color with `color`.

[Flood Fill](https://leetcode.com/problems/flood-fill)
```python
def floodFill(image, sr, sc, newColor):
    flood_fill(image, sr, sc, newColor)
    return image
```

#### [graph.**flood_fill_border**(*matrix*, *color*, *k=4*)](code/graph.py)

Flood fill the border of a `matrix` with `color`, where the nodes are `k`-directionally connected.

[Number of Enclaves](https://leetcode.com/problems/number-of-enclaves)
```python
def numEnclaves(A):
    flood_fill_border(A, 0)
    return sum(map(sum, A))
```

[Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands)
```python
def closedIsland(grid):
    flood_fill_border(grid, 1)
    return to_graph(grid, color=0).count_components()
```

[^1]: `(0, 0)`
[^2]: `(n - 1, n - 1)`
[^3]: they are different and they share an edge or a corner
[^4]: all the cells are `0`'s
[^5]: **Lexicographically smaller**: A string `a` is lexicographically smaller than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alien language than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.
[^6]: You are not on any bus initially
