import streamlit as st
from data_loader import load_data
from network_model import build_network, get_3d_layout
from contagion_engine import propagate_shock
from visualization import plot_3d_network
from metrics import compute_metrics
import numpy as np

st.set_page_config(page_title="3D Systemic Risk Contagion Engine", layout="wide", page_icon="💥", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    body {background-color: #18191A; color: #F5F6FA;}
    .stApp {background-color: #18191A;}
    </style>
    """, unsafe_allow_html=True)

st.title("3D Systemic Risk Contagion Engine")

# Sidebar controls
st.sidebar.header("Simulation Controls")
shock_asset = st.sidebar.selectbox("Shock Asset", options=None, index=0, key="shock_asset")
shock_magnitude = st.sidebar.slider("Shock Magnitude", 0.01, 1.0, 0.2, 0.01)
decay = st.sidebar.slider("Decay Speed", 0.0, 1.0, 0.5, 0.01)
corr_threshold = st.sidebar.slider("Correlation Threshold", 0.0, 1.0, 0.3, 0.01)
time_step = st.sidebar.slider("Time Step", 1, 20, 1, 1)
st.sidebar.header("Simulation Controls")


st.sidebar.markdown("""
###  Color Guide (Risk Intensity)
- 🔵 Blue → Low risk / low propagated impact  
- 🟣 Pink / Purple → Medium risk  
- 🟠 Orange → High risk  
- 🔴 Red / 🟡 Yellow → Extreme systemic stress (highest impact)
  

### How Simulation Works
- Shock starts from selected asset
- Risk spreads through correlated assets
- Decay speed reduces impact over time
- Colors update based on current stress level
""")


# Data loading
returns, asset_names = load_data()
if shock_asset is None:
    shock_asset = asset_names[0]

# Correlation/covariance/eigen
corr_matrix = np.corrcoef(returns, rowvar=False)
cov_matrix = np.cov(returns, rowvar=False)
eigvals, eigvecs = np.linalg.eigh(corr_matrix)

# Network construction
G = build_network(corr_matrix, asset_names, corr_threshold)
pos = get_3d_layout(G)

# Shock propagation
stress_levels = propagate_shock(G, asset_names, shock_asset, shock_magnitude, decay, time_step)

# Metrics
metrics = compute_metrics(G, stress_levels)

# Visualization
fig = plot_3d_network(G, pos, stress_levels, corr_matrix, metrics, animate=True, time_step=time_step)
st.plotly_chart(fig, use_container_width=True)

# Metrics display
st.subheader("Systemic Risk Metrics")
st.json(metrics)
