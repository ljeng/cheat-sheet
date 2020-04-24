## graph

### [class graph.**Graph**(*V*, *E*, *directed=True*)](/graph.py)

A `Graph` is a mathematical structure defined by a set of vertices `V` connected by edges `E`, where the distance from vertex `u` to vertex `v` is `E[u][v]`. A `Graph` can be `directed` or undirected. `Graph` objects support the following methods:

**count_components**()

Return the number of connected components.

[Number of Islands](https://leetcode.com/problems/number-of-islands)
```python
def numIslands(grid):
    return to_graph(grid, color='1').count_components()
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

**dijkstra**(*source*, *trace=False*)

Apply Dijkstra's algorithm. Return a dictionary in the form of `{u: distance}` where there is some `distance` from vertex `source` to vertex `u`. If `trace` is `True`, instead return a dictionary in the form of `{u: [[source...u]]}` where each list in the value is a path from `source` to `u`.

[Network Delay Time](https://leetcode.com/problems/network-delay-time)
```python
import collections


def networkDelayTime(times, N, K):
    E = collections.defaultdict(dict)
    for u, v, w in times:
        E[u][v] = w
    time = max(Graph(set(range(1, N + 1)), E).dijkstra(K).values())
    return int(time) if time < float('inf') else -1
```

[Bus Routes](https://leetcode.com/problems/bus-routes)
```python
import collections
import itertools


def numBusesToDestination(routes, S, T):
    E = collections.defaultdict(dict)
    for route in routes:
        for u, v in itertools.permutations(route, 2):
            if u != v:
                E[u][v] = 1
    dist = Graph(set(itertools.chain(*routes)), E).dijkstra(S)
    return dist[T] if T in dist and T < float('inf') else -1
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

**kruskal**()

Apply Kruskal's algorithm to an undirected graph. Return a minimum spanning tree `MST` in the form of a `collections.defaultdict(dict)` object, where the distance from vertex `u` to vertex `v` is `MST[u][v]`.

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
        

### [graph.**get_neighbors**(*matrix*, *i*, *j*, *color=None*, *k=4*)](/graph.py)]

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

### [graph.**to_graph**(*matrix*, *color=1*, *k=4*)](/graph.py)

Convert a `matrix` to a `Graph`. Each node is marked `color` and are `k`-directionally connected to its neighbors, where `k` can be 4 or 8.

### [graph.**flood_fill**(*matrix*, *i*, *j*, *color*, *k=4*)](/graph.py)

Flood fill a `matrix` in-place at coordinate `(i, j)` with `color`. Update `(i, j)` with `color`. Recursively update all `k`-directionally connected neighbors of `(i, j)` of the original color with `color`.

[Flood Fill](https://leetcode.com/problems/flood-fill)
```python
def floodFill(image, sr, sc, newColor):
    flood_fill(image, sr, sc, newColor)
    return image
```

### [graph.**flood_fill_border**(*matrix*, *color*, *k=4*)](/graph.py)

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

### [graph.**word_ladder**(*start*, *end*, *bank*, *trace=False*)](/graph.py)

Solve the problem:

> Given two words `start` and `end` and a word list `bank`, find the least number of transformations from `start` to `end`, such that only one letter can be changed at a time and each transformed word must exist in `bank`. `start` isn't necessarily a transformed word. All words have the same length.

If `trace` is `True`, this method will instead output all transformation sequences from `start` to `end`.

[Word Ladder II](https://leetcode.com/problems/word-ladder-ii)
```python
def findLadders(beginWord, endWord, wordList):
    return word_ladder(beginWord, endWord, wordList, trace=True)
```

[Word Ladder](https://leetcode.com/problems/word-ladder)
```python
def findLadderLength(beginWord, endWord, wordList):
    length = word_ladder(beginWord, endWord, wordList)
    return length + 1 if length < float('inf') else 0
```

[Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation)
```python
def minMutation(start, end, bank):
    mutations = word_ladder(start, end, bank)
    return mutations if mutations < float('inf') else -1
```