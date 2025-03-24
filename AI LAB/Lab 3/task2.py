from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,key,v):
        self.graph[key].append(v)

    def DFS(self,start,goal):
        visited = []
        queue = [start]
        loop_count = 0  # Count number of loops (operations)
        max_queue_size = 0
        while queue:
            loop_count += 1
            max_queue_size = max(max_queue_size, len(queue))
            s = queue.pop(0)
            visited.append(s)
            print(s, end=" ")
            if s == goal:
                print("\ngoal reached")
                break

            for i in self.graph[s]:
                if i not in visited:
                    queue.insert(0,i)
        print("\nTotal DFS Loops:", loop_count)
        print("Max Queue Size:", max_queue_size)


g=Graph()
g.addEdge("Home", "Products")
g.addEdge("Home", "Blogs")
g.addEdge("Home", "About Us")
g.addEdge("Home", "Contact Us")

g.addEdge("Products", "Product 1")
g.addEdge("Products", "Product 2")
g.addEdge("Products", "Product 3")

g.addEdge("Blogs", "Blog Post 1")
g.addEdge("Blogs", "Blog Post 2")
g.DFS("Home","Blog Post 2")




