from collections import defaultdict
import time


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_path_length = 0
        self.iterations = 0

    def addEdge(self, key, v):
        self.graph[key].append(v)

    def load_graph_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                self.graph = eval(data)
        except Exception as e:
            print(f"Error reading file: {e}")
            return {}

    def DLS(self, start, goal, depth_limit, depth=0, path=[]):
        self.iterations += 1
        path.append(start)
        self.max_path_length = max(self.max_path_length, len(path))

        if start == goal:
            print("\nGoal reached!")
            return True

        if depth >= depth_limit:
            path.pop()
            return False

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in path:
                    if self.DLS(neighbor, goal, depth_limit, depth + 1, path):
                        return True

        path.pop()
        return False

    def IDDFS(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            self.iterations = 0
            self.max_path_length = 0
            path = []
            print(f"Searching at depth {depth}...")
            if self.DLS(start, goal, depth, 0, path):
                print("Path to the word:", " -> ".join(path))
                print(f"Max Path Length: {self.max_path_length}")
                print(f"Iterations: {self.iterations}")
                return path

        print("Word not found within given depth limit.")
        return None


# Read graph from file
def read_graph(filename):
    graph = Graph()
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            if words:
                for word in words[1:]:
                    graph.addEdge(words[0], word)
    return graph


# Main execution
filename = "EnglishDictionary.txt"
graph = Graph()
graph.load_graph_from_file(filename)

start_word = input("Enter the starting word: ")
goal_word = input("Enter the word to search (goal): ")
depth_limit = int(input("Enter the maximum depth limit for search: "))

graph.IDDFS(start_word, goal_word, depth_limit)
