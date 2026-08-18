import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# Figure aur Axes setup
fig, ax = plt.subplots(figsize=(9, 5))

# Static Cost Curve plot karein
ax.plot(b_input, cost_input, color='blue', label='Cost Function')
ax.set_xlabel('Intercept (b)')
ax.set_ylabel('Cost')
ax.set_title('Gradient Descent Convergence on Cost Curve')

# Moving point initialization (Red Dot)
point, = ax.plot([], [], 'ro', markersize=8, label='Current b step')
line, = ax.plot([], [], 'r--', alpha=0.6)

# Data containers
xdata, ydata = [], []

def animate(i):
    label = f'Epoch {i + 1}'
    xdata.append(all_b[i])
    ydata.append(all_cost[i])
    
    # Point aur line trajectory update
    point.set_data([all_b[i]], [all_cost[i]])
    line.set_data(xdata, ydata)
    ax.set_xlabel(f'Intercept (b) - {label}')
    return point, line

# Animation object
anim = animation.FuncAnimation(fig, animate, frames=len(all_b), interval=400, repeat=False)

# Notebook me inline video render karne ke liye:
HTML(anim.to_jshtml())