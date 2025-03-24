import heapq
import math


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node, x, y):
        self.nodes[node] = (x, y)
        self.edges[node] = []

    def add_edge(self, n1, n2, w):
        self.edges[n1].append((n2, w))
        self.edges[n2].append((n1, w))

    def dist(self, n1, n2):
        x1, y1 = self.nodes[n1]
        x2, y2 = self.nodes[n2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def best_first_search(self, start, goal):
        priority_queue = []
        start_node = (0, start)
        heapq.heappush(priority_queue, start_node)
        prev = {start: None}
        visited = []
        loop_count = 0

        while priority_queue:
            loop_count += 1
            _, current = heapq.heappop(priority_queue)

            if current == goal:
                print(goal)
                print(f"Total nodes visited: {len(visited) + 1}")
                print(f"Total loop iterations: {loop_count}")
                return

            visited.append(current)
            print(f'{current} ', end="")

            for neighbor, cost in self.edges[current]:
                if neighbor not in visited:
                    heuristic = self.dist(neighbor, goal)
                    heapq.heappush(priority_queue, (heuristic, neighbor))
                    prev[neighbor] = current

        print(f"\nTotal nodes visited: {len(visited)}")
        print(f"Total loop iterations: {loop_count}")
        return None


graph = Graph()
graph.add_node("A", 0, 0)
graph.add_node("B", 2, 3)
graph.add_node("C", 5, 1)
graph.add_node("D", 7, 4)
graph.add_node("E", 8, 6)
graph.add_node("G", 10, 8)

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 3)
graph.add_edge("D", "E", 4)
graph.add_edge("E", "G", 2)

print("Fastest Path: ", end="")
graph.best_first_search("A", "G")
