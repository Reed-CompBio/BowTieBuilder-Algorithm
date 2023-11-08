import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_weighted_edges_from([(a, b, 0.5), (a, c, 0.8), (b, c, 1.2),
                          (b, d), 1.0, (c, e, 0.7), (d, e, 1.5), (e, f, 0.9)])

# Define the sets of nodes S and T
S = [a, b, c]
T = [d, e, f]

# Call the btb_implement function
pathway = btb_implement(S, T, G)

# Print the nodes and edges of the final pathway
print("Pathway Nodes:", pathway.nodes)
print("Pathway Edges:", pathway.edges(data=True))
