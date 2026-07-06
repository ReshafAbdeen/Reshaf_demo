#Machine Learning
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'Experience':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary':[15, 20, 25, 30, 55, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(f"Total Points : {len(X)}")
print(f"Training ke liye gye Points : {len(X_train)}")
print(f"Test ke liye bache Points : {len(X_test)}")

model = LinearRegression()
model.fit(X_train, y_train)

predicted_salaries = model.predict(X_test)

print("--- EXAM RESULTS ---")
print(f"Asli Salaries (Test Data): {y_test.values}")
print(f"Model ki Prediction:      {[round(float(num), 2) for num in predicted_salaries]}")