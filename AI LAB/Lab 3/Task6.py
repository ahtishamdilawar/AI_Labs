from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, key, v):
        self.graph[key].append(v)
        self.graph[v].append(key)

    def DFS(self, start, goal):
        visited = []
        stack = [start]
        loop_count = 0
        max_stack_size = 0

        while stack:
            loop_count += 1
            max_stack_size = max(max_stack_size, len(stack))
            s = stack.pop()
            visited.append(s)
            print(s, end=" ")

            if s == goal:
                print("\nGoal reached")
                break

            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)

        print("\nTotal DFS Loops:", loop_count)
        print("Max Stack Size:", max_stack_size)

    def BFS(self, start, goal):
        visited = set()
        queue = deque([start])
        loop_count = 0
        max_queue_size = 0

        while queue:
            loop_count += 1
            max_queue_size = max(max_queue_size, len(queue))
            s = queue.popleft()
            visited.add(s)
            print(s, end=" ")

            if s == goal:
                print("\nGoal reached")
                break

            for i in self.graph[s]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        print("\nTotal BFS Loops:", loop_count)
        print("Max Queue Size:", max_queue_size)

    def bidirectional_search(self, start, goal):
        if start == goal:
            print(f"Already at the goal: {goal}")
            return [start]

        forward_queue = deque([start])
        backward_queue = deque([goal])
        forward_visited = {start: None}
        backward_visited = {goal: None}
        intersection = None
        loop_count = 0
        max_queue_size = 0

        while forward_queue and backward_queue:
            loop_count += 1
            max_queue_size = max(max_queue_size, len(forward_queue) + len(backward_queue))

            if forward_queue:
                current = forward_queue.popleft()
                for neighbor in self.graph[current]:
                    if neighbor not in forward_visited:
                        forward_visited[neighbor] = current
                        forward_queue.append(neighbor)
                        if neighbor in backward_visited:
                            intersection = neighbor
                            break

            if backward_queue:
                current = backward_queue.popleft()
                for neighbor in self.graph[current]:
                    if neighbor not in backward_visited:
                        backward_visited[neighbor] = current
                        backward_queue.append(neighbor)
                        if neighbor in forward_visited:
                            intersection = neighbor
                            break

            if intersection:
                break

        if not intersection:
            print("No path found")
            return None

        path = []
        node = intersection
        while node:
            path.append(node)
            node = forward_visited[node]

        path.reverse()
        node = backward_visited[intersection]
        while node:
            path.append(node)
            node = backward_visited[node]

        print("\nPath found using Bidirectional Search:", " -> ".join(path))
        print("Total Bidirectional Search Loops:", loop_count)
        print("Max Queue Size:", max_queue_size)
        return path

# Create graph
g = Graph()
g.addEdge("Home", "Products")
g.addEdge("Home", "Blogs")
g.addEdge("Home", "About Us")
g.addEdge("Home", "Contact Us")
g.addEdge("Products", "Product 1")
g.addEdge("Products", "Product 2")
g.addEdge("Products", "Product 3")
g.addEdge("Blogs", "Blog Post 1")
g.addEdge("Blogs", "Blog Post 2")

g.bidirectional_search("Home", "Blog Post 2")
