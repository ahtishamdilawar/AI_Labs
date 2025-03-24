import heapq


class MarsRover:
    def __init__(self, terrain, start, goal):
        self.terrain = terrain
        self.start = start
        self.goal = goal
        self.rows = len(terrain)
        self.cols = len(terrain[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def heuristic(self, current):
        x1, y1 = current
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star(self):
        start = self.start
        goal = self.goal
        list = []
        heapq.heappush(list, (0 + self.heuristic(start), 0, start))  # (F, G, position)
        totalprev = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start)}
        closed_list = set()

        while list:
            _, current_g, current = heapq.heappop(list)

            if current == goal:
                path = []
                while current in totalprev:
                    path.append(current)
                    current = totalprev[current]
                path.append(start)
                path.reverse()
                return path, len(totalprev), len(list)

            closed_list.add(current)

            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)

                if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols and self.terrain[neighbor[0]][
                    neighbor[1]] != 1:
                    if neighbor in closed_list:
                        continue

                    future_g = current_g + 1

                    if neighbor not in g_score or future_g < g_score[neighbor]:
                        totalprev[neighbor] = current
                        g_score[neighbor] = future_g
                        f_score[neighbor] = future_g + self.heuristic(neighbor)
                        heapq.heappush(list, (f_score[neighbor], future_g, neighbor))

        return None, len(totalprev), len(list)



terrain = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

start = (0, 0)
goal = (5, 5)

obj = MarsRover(terrain, start, goal)
path, nodes_visited, iterations = obj.a_star()

if path:
    print("Path found:", path)
    print("Total nodes visited:", nodes_visited)
    print("Total iterations:", iterations)
else:
    print("No path found")
