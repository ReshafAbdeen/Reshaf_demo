import pandas as pd
import numpy as np

store_data = {
    "Item": ["ASUS TUF Laptop", "Logitech Mouse", "Ryzen 5 CPU", "ASUS TUF Laptop", "Logitech Mouse", "Mechanical Keyboard", "Ryzen 5 CPU"],
    "Category": ["Laptop", "Accessories", "Components", "Laptop", "Accessories", "Accessories", "Components"],
    "Quantity_Sold": [3, 10, 2, 1, 15, 5, None],  
    "Price_Per_Item": [75000, 15000, 18000, 75000, 1200, 4500, 18000],
    "Customer_Rating": [4.5, 4.2, 4.8, 4.6, None, 4.0, 4.7]
}

df = pd.DataFrame(store_data)
# print(df)

df["Quantity_Sold"] = df["Quantity_Sold"].fillna(0)

avg_rarting = df["Customer_Rating"].mean()
df["Customer_Rating"] = df["Customer_Rating"].fillna(avg_rarting)

df["Total_Revenue"] = df["Quantity_Sold"] * df["Price_Per_Item"]

category_sale = df.groupby("Category")["Total_Revenue"].sum()

print("\n----Cleaned data after processing----")
print(df)


print("\n----Sale by Category----")
print(category_sale)


best_item = df.loc[df["Quantity_Sold"].idxmax()]['Item']
print(f"\n----{best_item} Sabse mehga item----")