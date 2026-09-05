import collections


class Graph:

    def __init__(self):
        self.adj_list = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = {start}
        queue = collections.deque([start])
        order = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

print("BFS Traversal starting from 'A':")
print(" -> ".join(g.bfs("A")))