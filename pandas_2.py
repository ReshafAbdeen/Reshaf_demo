import pandas as pd
import numpy as np

# 1. Fake Sales Data create karna (Data Generation)
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Units_Sold': [10, 15, np.nan, 12, 8, 5, np.nan, 20],  # Kuch missing values dalen
    'Price_Per_Unit': [1000, 500, 300, 1000, 500, 300, 1000, 500],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West']
}
df = pd.DataFrame(data)

df['Units_Sold'] = df['Units_Sold'].fillna(0)

df['Total_Revenue'] = df['Units_Sold'] * df['Price_Per_Unit']

summary_df = df.groupby('Product').agg({'Units_Sold': 'sum', 'Total_Revenue': 'sum'}).reset_index()

summary_df.to_csv('product_sales_summary.csv', index=False)
print("--- Sales Summary Report ---")
print(summary_df)