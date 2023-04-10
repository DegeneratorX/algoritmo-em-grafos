from collections import deque

def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[2].split("=")[1])
        data = [tuple(map(int, line.strip().split())) for line in lines[4:]]
        return n, data

def write_data(components):
    for component in components:
        print(" ".join(str(node + 1) for node in component))

def find_connected_components(n, data):
    graph = {i: set() for i in range(n)}
    for x, y in data:
        graph[x - 1].add(y - 1)
        graph[y - 1].add(x - 1)

    visited = set()
    components = []
    for i in range(n):
        if i not in visited:
            component = set()
            bfs(i, graph, visited, component)
            components.append(sorted(component))

    return components

def bfs(start, graph, visited, component):
    queue = deque()
    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        component.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

for arqs in range(120):
    print()
    print(f"Arquivo {arqs}")
    n, data = read_data(f"{arqs}.in")
    components = find_connected_components(n, data)
    write_data(components)
    print()