from collections import defaultdict
from queue import Queue

def find_maximum_flow(graph, source, sink):
    max_flow = 0
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u, v, capacity in graph:
        residual_graph[u][v] += capacity

    parent = {}
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
    return max_flow, residual_graph


def bfs(graph, source, sink, parent):
    visited = {source}
    q = Queue()
    q.put(source)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                q.put(v)
                if v == sink:
                    return True
    return False


def compute_max_flow(graph):
    smallest_vertex = min(min(edge[0], edge[1]) for edge in graph)
    max_flow_values = []

    for vertex in range(1, len(graph) + 1):
        if vertex == smallest_vertex:
            continue
        max_flow, _ = find_maximum_flow(graph, smallest_vertex, vertex)
        max_flow_values.append((vertex, max_flow))

    return max_flow_values


# Input graph representation
graph = [
    [1, 3, 78.25],
    [2, 3, 76.75],
    [3, 5, 63.5],
    [3, 2, 51.25],
    [3, 1, 62.875],
    [4, 3, 13.625],
    [4, 2, 1.625],
    [4, 1, 14.125],
    [5, 2, 10.875],
    [5, 1, 40.0]
]

# Compute maximum flow values
max_flow_values = compute_max_flow(graph)

# Output the results
print(max_flow_values)