import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/ammishra008/Superstore-Sales-Analysis/main/superstore.csv'

print("\nE-Commerce Sales Data load ho raha hai, thoda sa sabr rakhein...")
df = pd.read_csv(url)
print("Data successfully load ho gaya!")
print(f"Total Transactions Ka Data: {df.shape[0]} Rows, {df.shape[1]} Columns\n")

print("--- Cleaning Missing Data ---")
df['Postal Code'] = df['Postal Code'].fillna(0)
df['Returns'] = df['Sales'].fillna(0) 
print("✔ Kachra saaf! Data ekdam ready hai.\n")

print("--- Top Product Categories by Sales ---")
category_sales = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
print(category_sales)

print("\nSales vs Profit Ka Graph taiyar ho raha hai...")
plt.figure(figsize=(10, 6))

sns.barplot(x='Category', y='Sales', data=category_sales, palette='dark:salmon_r')

plt.title("E-Commerce Sales Analysis by Category", fontsize=16, fontweight='bold')
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales (in USD)", fontsize=12)

print("Graph aapki screen par khulne wala hai...")
plt.show()