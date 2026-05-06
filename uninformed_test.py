import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs


graph = {
    'A': ['B', 'C'],     # Level 0 to Level 1
    'B': ['D', 'E'],     # Level 1 to Level 2
    'C': ['F'],          # Level 1 to Level 2
    'D': [],             # Leaf node (Level 2)
    'E': ['G'],          # Level 2 to Level 3
    'F': [],             # Leaf node (Level 2)
    'G': []              # Leaf node (Level 3)
}


G = nx.DiGraph()


for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)


plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))
print("IDDFS:", iddfs(graph, 'A', 3))  # max_depth = 3 (levels 0-3)