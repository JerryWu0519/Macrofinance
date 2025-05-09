import numpy as np
import pandas as pd
from functions import optimize_sharpe, compute_returns

def rolling_sharpe_backtest(prices, window=252, test_horizon=21):
    from functions import compute_returns, optimize_sharpe
    import pandas as pd

    returns = compute_returns(prices)
    dates = returns.index

    oos_returns = []
    all_weights = []

    for start in range(0, len(dates) - window - test_horizon, test_horizon):
        train = returns.iloc[start:start+window]
        test = returns.iloc[start+window:start+window+test_horizon]

        try:
            weights = optimize_sharpe(train)
        except:
            continue

        # Store weights with date of rebalance
        weights.name = dates[start+window]  # mark rebalance date
        all_weights.append(weights)

        # Align test columns
        test = test[weights.index]

        # Compute OOS return
        port_return = test @ weights
        oos_returns.extend(port_return.values)

    # Format outputs
    idx = dates[window:window+len(oos_returns)]
    oos_series = pd.Series(oos_returns, index=idx)
    weights_df = pd.DataFrame(all_weights)

    return oos_series, weights_df
