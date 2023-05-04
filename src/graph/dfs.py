def dfs(graph, vertex, seen):
    """
    dfs
    """
    seen[vertex] = True

    # Output something. Change as needed.
    print(vertex, end= " ")

    # Visit all descendant.
    for next_v in graph[vertex]:
        # Skip visited vertices.
        if seen[next_v] == True:
            continue
        dfs(graph, next_v, seen)