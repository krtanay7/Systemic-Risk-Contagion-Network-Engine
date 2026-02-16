import numpy as np

def propagate_shock(G, asset_names, shock_asset, shock_magnitude, decay, time_step):
    # Initialize stress
    stress = {name: 0.0 for name in asset_names}
    stress[shock_asset] = shock_magnitude
    for t in range(time_step):
        new_stress = stress.copy()
        for node in G.nodes:
            for neighbor in G.neighbors(node):
                edge_weight = abs(G[node][neighbor]['weight'])
                # Propagate stress
                new_stress[neighbor] += stress[node] * edge_weight * (1 - decay)
        # Decay
        for node in new_stress:
            new_stress[node] *= (1 - decay)
        stress = new_stress
    return stress
