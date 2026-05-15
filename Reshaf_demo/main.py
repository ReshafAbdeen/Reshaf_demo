#I'M WRITE A RAINBOW SPIRAL DESIGN (GRAPHICS)

import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Black")
t.speed(0)

n = 36
h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h -= n/2
    t.color(c)

    t.forward(i * 2)
    t.right(170)

turtle.done()  





#I'M USE PANDAS LIBRARY FIRST TIME IN MY 30 DAYS PYTHON JOURNEY.
import pandas as pd 

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Mouse', 'Keyboard', None],
    'Price': [50000, 500, 15000, 52000, 600, 2000, 0],
    'Quantity': [2, 5, 1, 1, 10, 3, 0],
    'Store': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

df = df.dropna() 

df['Total_Sales'] = df['Price'] * df['Quantity']

store_report = df.groupby('Store')['Total_Sales'].sum()

top_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

print("--- Cleaned Data ---")
print(df)

print("\n--- Store Wise Sales ---")
print(store_report)

print("\n--- Top Selling Products (By Quantity) ---")
print(top_product)







