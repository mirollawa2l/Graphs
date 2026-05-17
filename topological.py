from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.reverse()
        return stack

g = Graph(8)
edges = [
    (0, 1), (1, 2), (1, 5), (2, 6), (3, 1),
    (3, 5), (4, 6), (5, 6), (6, 7)
]

for u, v in edges:
    g.add_edge(u, v)

# Print the topological sort result
print("Topological Sort:", g.topological_sort())
