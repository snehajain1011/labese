state_space = {
    "(0,0)" : ["(0,3)", "(4,0)"],
    "(0,3)" : ["(3,0)", "(4,3)"],
    "(4,0)" : ["(4,3)", "(1,3)"],
    "(3,0)" : ["(3,3)", "(0,3)"],
    "(4,3)" : ["(0,3)", "(4,0)"],
    "(1,3)" : ["(4,0)", "(1,0)"],
    "(3,3)" : ["(4,2)"],
    "(1,0)" : ["(0,1)"],
    "(4,2)" : ["(0,2)"],
    "(0,1)" : ["(4,1)"],
    "(0,2)" : [],
    "(4,1)" : ["(2,3)"],
    "(2,3)" : ["(2,0)"],
    "(2,0)" : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)

        if m == "(2,0)":
            print(f"{m} = [Goal State]", end=" ")
        else:
            print(m, end=" , ")

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

print("BFS: ")
bfs(visited, state_space, "(0,0)")
