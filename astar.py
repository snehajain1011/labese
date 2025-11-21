import numpy as np
import heapq

warehouse = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]])

ROBOT_START = (0, 0)
PICKUP_P = (2, 2)
DROP_D = (7, 7)

GRID_HEIGHT, GRID_WIDTH = warehouse.shape
OBSTACLE_CODE = 1

def is_valid_location(x, y):
    if not (0 <= x < GRID_HEIGHT and 0 <= y < GRID_WIDTH):
        return False
    return warehouse[x, y] != OBSTACLE_CODE

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(start, goal):
    frontier = [(0, 0, start)]
    g_cost = {start: 0}
    came_from = {start: None}

    while frontier:
        f_cost, current_g, current_node = heapq.heappop(frontier)

        if current_node == goal:
            return came_from, current_g

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x, neighbor_y = current_node[0] + dx, current_node[1] + dy
            neighbor = (neighbor_x, neighbor_y)

            if is_valid_location(neighbor_x, neighbor_y):
                new_g_cost = current_g + 1

                if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_g_cost
                    h_cost = heuristic(neighbor, goal)
                    f_cost = new_g_cost + h_cost
                    
                    heapq.heappush(frontier, (f_cost, new_g_cost, neighbor))
                    came_from[neighbor] = current_node
    
    return None, None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    if not came_from or current not in came_from:
        return None
        
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

came_from_1, cost_1 = a_star_search(ROBOT_START, PICKUP_P)
path_1 = reconstruct_path(came_from_1, ROBOT_START, PICKUP_P)

came_from_2, cost_2 = a_star_search(PICKUP_P, DROP_D)
path_2 = reconstruct_path(came_from_2, PICKUP_P, DROP_D)

print("Grid:")
print(warehouse)

print("\nStart", ROBOT_START, "to Pickup", PICKUP_P)
if path_1:
    print(f"Cost 1 (S->P): {cost_1}")
    print("Path 1:", " -> ".join(map(str, path_1)))
else:
    print("Path 1 not found (Pickup location is unreachable).")


print("\nPickup", PICKUP_P, "to Drop-off", DROP_D)
if path_2:
    print(f"Cost 2 (P->D): {cost_2}")
    print("Path 2:", " -> ".join(map(str, path_2)))
else:
    print("Path 2 not found (Drop location is unreachable from Pickup).")

if path_1 and path_2:
    total_cost = cost_1 + cost_2
    full_path = path_1 + path_2[1:] 
    print(f"Total Cost: {total_cost} steps")
    print("Full Path:", " -> ".join(map(str, full_path)))
else:
    print("The complete path could not be found.")