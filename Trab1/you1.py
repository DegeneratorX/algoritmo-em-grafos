def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[2].split("=")[1])
        data = [tuple(map(int, line.strip().split())) for line in lines[4:]]
        return n, data


def write_data(components):
    for component in components:
        print(" ".join(str(node) for node in component))


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
            dfs(i, graph, visited, component)
            components.append(sorted(component))

    return components


def dfs(node, graph, visited, component):
    visited.add(node)
    component.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)


for arqs in range(120):
    print()
    print(f"Arquivo {arqs}")
    n, data = read_data(f"{arqs}.in")
    components = find_connected_components(n, data)

    # map the nodes to the components they belong to
    node_component = {node: i for i, component in enumerate(
        components) for node in component}

    # output the components in the desired format
    max_component = max(node_component.values())
    output = [[] for _ in range(max_component + 1)]
    for node in range(n):
        output[node_component[node]].append(str(node + 1))

    write_data(output)
    print()