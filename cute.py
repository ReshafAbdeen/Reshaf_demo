import matplotlib.pyplot as plt

# Plotting Cost vs Intercept (b)
plt.figure(figsize=(9, 5))
plt.plot(b_input, cost_input, color='red', linewidth=2)
plt.title('Cost Function Curve (b vs Cost)')
plt.xlabel('Intercept (b)')
plt.ylabel('Cost / Loss')
plt.grid(True)
plt.show()