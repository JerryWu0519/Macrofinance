from functions2 import rolling_sharpe_backtest
from data_reading import load_price_data

# Load and backtest
data = load_price_data()
oos, weights_df = rolling_sharpe_backtest(data)

# Output performance
print("Mean return:", oos.mean())
print("Std dev:", oos.std())
print("Sharpe ratio:", oos.mean() / oos.std())

# Print weights
print("\n📊 Portfolio Weights at Each Rebalance:")
# Show all portfolio weights over time
print(weights_df.fillna(0).round(3))

# Optional: save to CSV
weights_df.to_csv("weights_over_time.csv")

# Plot performance
import matplotlib.pyplot as plt
(oos + 1).cumprod().plot(title="Out-of-Sample Cumulative Return", figsize=(10,5))
plt.grid()
plt.show()
