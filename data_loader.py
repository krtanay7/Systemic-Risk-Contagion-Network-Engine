import numpy as np
import pandas as pd

def load_data():
    # For demo: generate synthetic returns for 20 assets, 500 days
    np.random.seed(42)
    n_assets = 20
    n_days = 500
    asset_names = [f"Asset_{i+1}" for i in range(n_assets)]
    # Simulate correlated returns
    base = np.random.normal(0, 1, (n_days, 1))
    returns = base + np.random.normal(0, 0.5, (n_days, n_assets))
    return returns, asset_names
