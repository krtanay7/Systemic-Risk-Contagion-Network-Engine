import networkx as nx
import numpy as np

def build_network(corr_matrix, asset_names, threshold=0.3):
    G = nx.Graph()
    for i, name in enumerate(asset_names):
        G.add_node(name)
    n = len(asset_names)
    for i in range(n):
        for j in range(i+1, n):
            if abs(corr_matrix[i, j]) >= threshold:
                G.add_edge(asset_names[i], asset_names[j], weight=corr_matrix[i, j])
    return G

def get_3d_layout(G):
    # Use spring layout in 3D
    pos = nx.spring_layout(G, dim=3, seed=42)
    return pos
