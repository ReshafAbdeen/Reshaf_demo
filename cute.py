import pandas as pd
import numpy as np

# Sample Messy Sales Data Frame
data = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106],
    'Region': ['North', 'South', 'North', 'East', np.nan, 'West'],
    'Sales': [2500, 1800, np.nan, 3200, 4100, 2900],
    'Quantity': [5, 3, 4, np.nan, 6, 2],
    'Discount_Pct': [10, 5, 0, 15, 20, 0]
}

df = pd.DataFrame(data)

# 1. Missing Values Handle Karein
df['Region'] = df['Region'].fillna('Unknown')
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
df['Quantity'] = df['Quantity'].fillna(1)

# 2. Vectorized Feature Creation (NumPy Conditionals)
df['Unit_Price'] = df['Sales'] / df['Quantity']
df['Performance'] = np.where(df['Sales'] > 3000, 'High', 'Standard')

# 3. GroupBy Aggregation
summary = df.groupby('Region').agg(
    Total_Sales=('Sales', 'sum'),
    Avg_Unit_Price=('Unit_Price', 'mean'),
    Transaction_Count=('Transaction_ID', 'count')
).reset_index()

print("--- Cleaned DataFrame ---")
print(df[['Transaction_ID', 'Region', 'Sales', 'Performance']])

print("\n--- Region Summary ---")
print(summary)