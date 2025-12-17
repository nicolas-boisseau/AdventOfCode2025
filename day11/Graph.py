import heapq
from functools import lru_cache


class Graph:
    def __init__(self):
        # Dictionary to store adjacency list: {node: [(neighbor, weight), ...]}
        self.adjacency = {}

    def add_edge(self, u, v, weight=1):
        """Add an edge to the graph (undirected by default)."""
        if weight < 0:
            raise ValueError("Edge weights must be non-negative for Dijkstra's algorithm.")
        self.adjacency.setdefault(u, []).append((v, weight))
        #self.adjacency.setdefault(v, []).append((u, weight))  # Remove if directed graph

    def shortest_path(self, start, target):
        """Find shortest path from start to target using Dijkstra's algorithm."""
        if start not in self.adjacency or target not in self.adjacency:
            raise ValueError("Start or target node not found in the graph.")

        # Priority queue: (distance, node, path)
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            dist, node, path = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)

            if node == target:
                return dist, path  # Found shortest path

            for neighbor, weight in self.adjacency.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (dist + weight, neighbor, path + [neighbor]))

        return float("inf"), []  # No path found

    def find_all_paths(self, start, target, path=[]):
        """Find all paths from start to target using DFS."""
        path = path + [start]
        if start == target:
            return [path]
        if start not in self.adjacency:
            return []
        paths = []
        for neighbor, _ in self.adjacency[start]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, target, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    @lru_cache(maxsize=None)
    def count_all_paths(self, start, target, dac_fft_checked=(False, False)):
        """Find all paths from start to target using DFS."""
        if start == target:
            if dac_fft_checked == (True, True):
                return 1
            else:
                return 0

        if start == "dac" and not dac_fft_checked[0]:
            dac_fft_checked = (True, dac_fft_checked[1])
        if start == "fft" and not dac_fft_checked[1]:
            dac_fft_checked = (dac_fft_checked[0], True)

        if start not in self.adjacency:
            return 0

        count = 0
        for neighbor, _ in self.adjacency[start]:
            subCount = self.count_all_paths(neighbor, target, dac_fft_checked)
            count += subCount

        return count



# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)

    distance, path = g.shortest_path("A", "E")
    print(f"Shortest distance: {distance}")
    print(f"Path: {' -> '.join(path)}")
