# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def BFS(self, s):
#         visited = [False] * (max(self.graph) + 1)
#         print(len(self.graph))
#
#         queue = []
#
#         queue.append(s)
#         visited[s] = True
#
#         while queue:
#
#             s = queue.pop(0)
#             print(s, end=" ")
#
#
#             for i in self.graph[s]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True
#
# g = Graph()
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 5)
# g.addEdge(3, 6)
# g.addEdge(3, 7)
# g.addEdge(2, 1)
# g.addEdge(3, 1)
# g.addEdge(4, 2)
# g.addEdge(5, 2)
# g.addEdge(6, 3)
# g.addEdge(7, 3)
#
# print("BFS from vertex 5 is")
# g.BFS(5)
