# functions.py
import numpy as np
import pandas as pd
from scipy.optimize import minimize

def clean_data(data, min_valid=0.1):
    # Drop columns with too many missing values
    data = data.dropna(axis=1, thresh=len(data) * min_valid)
    data = data.ffill().bfill()
    return data

def compute_returns(data):
    return data.pct_change().dropna()

def optimize_sharpe(returns):
    mu = returns.mean()
    cov = returns.cov()
    n = len(mu)

    def negative_sharpe(weights):
        ret = np.dot(weights, mu)
        vol = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
        return -ret / vol

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(n))
    init_guess = np.ones(n) / n

    opt = minimize(negative_sharpe, init_guess,
                   method='SLSQP',
                   bounds=bounds,
                   constraints=constraints)

    return pd.Series(opt.x, index=mu.index)
