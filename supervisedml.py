#Machine Learning

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

data = {
    'Experience':[1, 2, 3, 4, 5],
    'Salary':[15, 20, 25, 30, 55]
}

df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)
print("Model Train ho Gya hai")

new_data = pd.DataFrame({"Experience":[6, 8]})
predicted_salaries = model.predict(new_data)

print(f"6 saal ke experience wale ki predicted salary: {predicted_salaries[0]:.2f}k")
print(f"8 saal ke experience wale ki predicted salary: {predicted_salaries[1]:.2f}k")