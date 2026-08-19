import numpy as np
import plotly.graph_objects as go

# 1. Parameter Grid Create karein (m aur b)
m_vals = np.linspace(-100, 100, 50)
b_vals = np.linspace(-150, 150, 50)
M, B = np.meshgrid(m_vals, b_vals)

# 2. Har (m, b) pair ke liye Cost calculate karein
X_arr = np.array(X).ravel()
y_arr = np.array(y).ravel()

Z = np.zeros(M.shape)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        Z[i, j] = np.sum((y_arr - (M[i, j] * X_arr + B[i, j])) ** 2)

# 3. Interactive 3D Surface Plot Render karein
fig = go.Figure(data=[go.Surface(z=Z, x=M, y=B, colorscale='Viridis')])

fig.update_layout(
    title='3D Cost Surface (m vs b vs Cost)',
    scene=dict(
        xaxis_title='Slope (m)',
        yaxis_title='Intercept (b)',
        zaxis_title='Cost'
    ),
    width=800,
    height=600
)

fig.show()