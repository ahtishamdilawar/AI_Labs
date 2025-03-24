import heapq

class Node:
    def __init__(self, state, cost, parent):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost


def uniform_cost_search(initial_state, goal_state, graph):
    visited = set()
    frontier = []
    heapq.heappush(frontier, Node(initial_state, 0, None))

    nodes_expanded = 0  # For time complexity
    max_frontier_size = 0  # For space complexity


    while frontier:
        max_frontier_size = max(max_frontier_size, len(frontier))  # Track max space used

        current_node = heapq.heappop(frontier)
        nodes_expanded += 1

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            print(f" Path to goal: {' -> '.join(path[::-1])}")
            print(f"Time iterations: {nodes_expanded}")
            print(f"️ Max frontier size: {max_frontier_size}")
            return path[::-1]

        visited.add(current_node.state)

        for neighbor, cost in graph.get(current_node.state, []):
            if neighbor not in visited:
                heapq.heappush(frontier, Node(neighbor, current_node.cost + cost, current_node))

    print("not reachable")
    return None


graph = {
    "Faisalabad": [("Lahore", 2), ("Chiniot", 1), ("Islamabad", 4), ("Sargodha", 2)],
    "Lahore": [("Islamabad", 5), ("Faisalabad", 2)],
    "Chiniot": [("Islamabad", 6), ("Lahore", 3)],
    "Rawalpindi": [("Islamabad", 1), ("Murree", 1)]
}

start_city = "Faisalabad"
goal_city = "Islamabad"

uniform_cost_search(start_city, goal_city, graph)
