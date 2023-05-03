from queue import Queue

def bfs():
    """bfs"""
    num_v, num_l = map(int, input().split())
    # Make adjacency list.
    g = [[] for _ in range(num_v)]
    for _ in range(num_l):
        v1, v2 = map(int, input().split())
        # Connect two vertices to each other.
        g[v1].append(v2)
        g[v2].append(v1)

    distance = [-1] * num_v
    que = Queue()

    nodes_i_th_scanned = [[] for _ in range(num_v)]
    # Initialize vertex0.
    nodes_i_th_scanned[0] = [0]
    distance[0] = 0
    que.put(0)

    # Scan all vertices.
    while not que.empty():
        v = que.get()
        # Scan adjacent vertices.
        for next_v in g[v]:
            # Skip if adjacent vertex has been searched.
            if distance[next_v] != -1:
                continue

            # Update distances of adjacent vertices. 1 greater than the vertex under Scan.
            distance[next_v] = distance[v] + 1
            # Manage the i-th scanned vertex
            nodes_i_th_scanned[distance[next_v]].append(next_v)

            que.put(next_v)     