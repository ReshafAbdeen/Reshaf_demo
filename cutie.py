import pandas as pd
import numpy as np

customers = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'Region': ['North', 'South', 'East', 'West']
})

sales = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 101, 104, 105], 
    'Amount': [250.0, 150.0, 300.0, np.nan, 400.0], 
    'Category': ['Tech', 'Apparel', 'Tech', 'Books', 'Toys']
})

df = pd.merge(sales, customers, on='CustomerID', how='left')

avg_sale = df['Amount'].mean()
df['Amount'] = df['Amount'].fillna(avg_sale)

df['Region'] = df['Region'].fillna('Unknown')

pivot_summary = pd.pivot_table(
    df, values='Amount', index='Region', columns='Category', 
    aggfunc='sum', fill_value=0
)

print(pivot_summary)