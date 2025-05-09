from data_reading import load_price_data
from functions import compute_returns, optimize_sharpe

# Load data
data = load_price_data()

# Compute returns and optimize
returns = compute_returns(data)
weights = optimize_sharpe(returns)

# Display results
weights = weights[weights > 0.0000000000000000000000000000000000000000000000000001].sort_values(ascending=False)
print("Optimal Sharpe Ratio Portfolio:")
print(weights)
