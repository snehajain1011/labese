import heapq

def manhattan(state):
    dist = 0
    for i in range(9):
        if state[i] == 0:
            continue
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(state[i], 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = divmod(zero, 3)
    moves = []
    if x > 0: moves.append((-1, 0))
    if x < 2: moves.append((1, 0))
    if y > 0: moves.append((0, -1))
    if y < 2: moves.append((0, 1))
    for dx, dy in moves:
        newx, newy = x + dx, y + dy
        new_zero = newx * 3 + newy
        new_state = state[:]
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(new_state)
    return neighbors

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan(start), start))
    came_from = {tuple(start): None}
    g_cost = {tuple(start): 0}
    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            return reconstruct_path(came_from, current)
        for nxt in get_neighbors(current):
            nxt_t = tuple(nxt)
            new_cost = g_cost[tuple(current)] + 1
            if nxt_t not in g_cost or new_cost < g_cost[nxt_t]:
                g_cost[nxt_t] = new_cost
                priority = new_cost + manhattan(nxt)
                heapq.heappush(pq, (priority, nxt))
                came_from[nxt_t] = current
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while came_from[tuple(current)] is not None:
        current = came_from[tuple(current)]
        path.append(current)
    path.reverse()
    return path

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal  = [1, 2, 3,
         4, 5, 6,
         7, 8, 0]

path = a_star(start, goal)

for p in path:
    print(p[0:3])
    print(p[3:6])
    print(p[6:9])
    print("-----------")
