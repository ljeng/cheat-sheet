import heapq


class Digraph:

	def __init__(self, vertices, edges):
		# vertices type = iterable
		# edges type = adjacency dict
		self.vertices, self.edges = vertices, edges

	def djikstras(self, source):
		distance = {u: float('inf') for u in self.vertices}
		distance[source] = 0
		priority_queue = [(0, source)]
		while priority_queue:
			d1, u = heapq.heappop(priority_queue)
			if d1 <= distance[u]:
				for v in self.edges[u]:
					d2 = d1 + self.edges[u][v]
					distance[v] = min(distance[v], d2)
					heapq.heappush(priority_queue, (d2, v))
		return distance

	def bellman_ford(self, source):
		distance = {u: float('inf') for u in self.vertices}
		distance[source] = 0
		predecessor = {u: None for u in self.vertices}
		for w in self.vertices:
			for u in self.edges:
				for v in self.edges[u]:
					if distance[u] + self.edges[u][v] < distance[v]:
						distance[v] = distance[u] + self.edges[u][v]
						predecessor[v] = u
		return distance

	def floyd_warshall(self):
		distance = {u: {v: float('inf') for v in self.vertices} for u in self.vertices}
		for u in self.vertices: distance[u][u] = 0
		for u in self.edges:
			for v in self.edges[u]: distance[u][v] = self.edges[u][v]
		for v in self.edges:
			for u in self.edges:
				if v in self.edges[u]:
					for w in self.edges[v]:
						distance[u][w] = min(distance[u][w], distance[u][v] + distance[v][w])
		# output type = adjacency dict
		return distance