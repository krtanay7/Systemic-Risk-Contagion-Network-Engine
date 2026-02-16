# 3D Systemic Risk Contagion Engine

A modular Streamlit application to model and visualize **financial contagion** across interconnected assets in 3D.

<img width="2997" height="1464" alt="systematic" src="\prototype\Engine.png" />

---

## 🌐 Live Demo

🔗 https://systemic-risk-contagion-network-engine.streamlit.app/


## Systemic Risk Modeling

Systemic risk is the risk of collapse of an entire financial system due to the failure of a single entity or group. This engine models how shocks to one asset propagate through a network of correlated assets, helping identify vulnerabilities and systemically important nodes.

This engine models:

- Correlation-based asset networks
- Shock propagation through connected nodes
- Risk diffusion with decay over time
- Identification of systemically important assets

The simulation helps visualize how local shocks can evolve into network-wide contagion.

---

## Features

- Load real or synthetic asset returns
- Compute correlation and covariance matrices
- Eigenvalue decomposition for risk structure analysis
- Build a 3D asset network (nodes = assets, edges = correlations)
- Simulate shock propagation with decay dynamics
- Interactive simulation controls:
  - Shock Asset
  - Shock Magnitude
  - Decay Speed
  - Correlation Threshold
  - Time Step
- Systemic risk metrics:
  - Network Density
  - Centrality
  - Systemic Importance Ranking
- Dark institutional-grade 3D visualization

---

## Color Guide (Risk Intensity)

- Blue -> Low propagated stress
- Pink / Purple -> Medium stress
- Orange -> High stress
- Red / Yellow -> Maximum systemic stress

Note: Colors represent **normalized relative stress levels**.

---

## How the Simulation Works

1. A shock is applied to a selected asset.
2. Risk propagates through correlated connections.
3. Decay reduces impact over time.
4. Stress levels update dynamically at each time step.
5. Node colors represent current risk intensity.

---

##  Tech Stack

- **Python** — Core simulation logic and systemic risk modeling  
- **Streamlit** — Interactive dashboard and UI controls  
- **NumPy** — Numerical computation and matrix operations  
- **Plotly** — Interactive 3D visualization and analytics rendering  
- **NetworkX** — Asset network construction and graph-based analysis  

---


## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the app

```bash
python -m streamlit run app.py
```

---

## Project Structure

- `app.py`: Streamlit UI entry point
- `data_loader.py`: Data loading/generation
- `network_model.py`: Network construction and layout
- `contagion_engine.py`: Shock propagation logic
- `visualization.py`: 3D Plotly visualization
- `metrics.py`: Systemic risk metrics
- `requirements.txt`: Dependencies
- `README.md`: Project overview

---

## Research Perspective

This project is inspired by concepts from **network science**, **systemic risk modeling**, and **financial contagion theory**.

Instead of treating assets independently, the system models markets as an interconnected network where shocks propagate through correlation-based relationships.

The engine allows experimentation with key research ideas such as:

- Shock diffusion across complex networks
- Impact decay over time
- Correlation-driven contagion dynamics
- Identification of systemically important nodes
- Sensitivity analysis using controllable parameters

The objective is to transform theoretical systemic risk concepts into an interactive visual experiment that supports intuitive exploration and analytical reasoning.
