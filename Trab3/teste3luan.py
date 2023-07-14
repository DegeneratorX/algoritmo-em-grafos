import networkx as nx

# Define the directed graph
edges = [
    [1, 3, 78.25],
    [2, 3, 76.75],
    [3, 5, 63.5],
    [3, 2, 51.25],
    [3, 1, 62.875],
    [4, 3, 13.625],
    [4, 2, 1.625],
    [4, 1, 14.125],
    [5, 2, 10.875],
    [5, 1, 40.0],
]

# Create a directed graph
G = nx.DiGraph()

# Add edges and their weights to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], capacity=edge[2])

# Get the vertices
vertices = G.nodes()

# Compute maximum flow values
for t in sorted(vertices):
    if t != 1:  # Skip the start node
        flow_value, flow_dict = nx.maximum_flow(G, 1, t)
        print(f"{t} {flow_value}")