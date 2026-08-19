import plotly.graph_objects as go

# 1. Base 3D Surface Plot
fig = go.Figure(data=[
    go.Surface(
        z=Z, x=M, y=B, 
        colorscale='Viridis', 
        opacity=0.8,
        name='Cost Surface'
    )
])

# 2. Gradient Descent Trajectory (3D Line + Points)
fig.add_trace(
    go.Scatter3d(
        x=all_m, 
        y=all_b, 
        z=all_cost,
        mode='lines+markers',
        marker=dict(size=5, color='red', symbol='circle'),
        line=dict(color='red', width=4),
        name='GD Trajectory'
    )
)

# 3. Layout Configuration
fig.update_layout(
    title='Gradient Descent Trajectory on 3D Cost Surface',
    scene=dict(
        xaxis_title='Slope (m)',
        yaxis_title='Intercept (b)',
        zaxis_title='Cost'
    ),
    width=850,
    height=650
)

fig.show()