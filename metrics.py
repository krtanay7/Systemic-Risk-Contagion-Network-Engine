import networkx as nx

def compute_metrics(G, stress_levels):
    density = nx.density(G)
    centrality = nx.eigenvector_centrality_numpy(G)
    ranking = sorted(stress_levels.items(), key=lambda x: x[1], reverse=True)
    return {
        'Network Density': density,
        'Centrality': centrality,
        'Systemic Importance Ranking': ranking
    }
