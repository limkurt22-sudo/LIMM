"""Assessment 3.3: Graph using the last name LIM.

Each letter is a vertex. Edges: L-I, L-M, I-M.
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        if b not in self.adjacency[a]:
            self.adjacency[a].append(b)
        if a not in self.adjacency[b]:
            self.adjacency[b].append(a)

    # ---------- BFS (queue) ----------
    def bfs(self, start):
        visited = [start]
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in sorted(self.adjacency[vertex]):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    # ---------- DFS (recursion / stack) ----------
    def dfs(self, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for neighbor in sorted(self.adjacency[start]):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited


def arrow(items):
    return " -> ".join(items)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("L", "I")
    graph.add_edge("L", "M")
    graph.add_edge("I", "M")

    print("GRAPH (LIM)")
    print("      L")
    print("     / \\")
    print("    I---M")
    print()
    print("Adjacency List:")
    for vertex, neighbors in graph.adjacency.items():
        print(f"  {vertex}: {', '.join(neighbors)}")
    print()
    print("BFS starting at L:", arrow(graph.bfs("L")))
    print("DFS starting at L:", arrow(graph.dfs("L")))