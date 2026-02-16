import plotly.graph_objs as go
import numpy as np

def plot_3d_network(G, pos, stress_levels, corr_matrix, metrics, animate=True, time_step=1):
    node_x = []
    node_y = []
    node_z = []
    node_size = []
    node_color = []
    labels = []
    for node in G.nodes:
        x, y, z = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)
        node_size.append(10 + 40 * stress_levels[node])
        node_color.append(stress_levels[node])
        labels.append(node)
    edge_x = []
    edge_y = []
    edge_z = []
    for edge in G.edges:
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_z += [z0, z1, None]
    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        mode='lines',
        line=dict(color='#888', width=2),
        hoverinfo='none')
    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers+text',
        marker=dict(
            size=node_size,
            color=node_color,
            colorscale='Inferno',
            cmin=0, cmax=max(node_color),
            line=dict(width=2, color='white'),
            opacity=0.95
        ),
        text=labels,
        textposition='top center',
        hoverinfo='text')
    layout = go.Layout(
        title='3D Systemic Risk Contagion Network',
        showlegend=False,
        margin=dict(l=0, r=0, b=0, t=40),
        paper_bgcolor='#18191A',
        plot_bgcolor='#18191A',
        scene=dict(
            xaxis=dict(showbackground=False, color='#F5F6FA'),
            yaxis=dict(showbackground=False, color='#F5F6FA'),
            zaxis=dict(showbackground=False, color='#F5F6FA'),
        ),
        font=dict(color='#F5F6FA', size=14)
    )
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
    return fig
