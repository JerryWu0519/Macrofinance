from data_reading import load_price_data

# Load the data
data = load_price_data()

# 📊 View the result
print("\n✅ Data loaded!")
print(f"Shape: {data.shape}")
print("Columns (assets):", list(data.columns))
print("\nPreview:")
print(data.head())

# If you want a quick look at any missing values:
print("\nMissing values per column:")
print(data.isna().sum())
