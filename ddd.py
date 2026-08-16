import numpy as np

# Intercept values range
b_input = np.linspace(-150, 150, 100)
cost_input = []

# X aur y ko reset karke clean 1D array banayein
X_arr = np.array(X).ravel()
y_arr = np.array(y).ravel()

# Single Loop (No nested j-loop)
for i in range(len(b_input)):
    # Direct vectorized cost calculation
    this_cost = np.sum((y_arr - m * X_arr - b_input[i]) ** 2)
    cost_input.append(this_cost)

print("Success! Calculated", len(cost_input), "cost values.")