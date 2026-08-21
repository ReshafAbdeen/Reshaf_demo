import plotly.graph_objects as go

# Contour Plot with GD Steps Overlay
fig = go.Figure()

# 1. Background Contour map
fig.add_trace(go.Contour(
    z=Z, x=m_vals, y=b_vals,
    colorscale='Jet',
    contours_coloring='heatmap',
    line_width=1
))

# 2. Gradient Descent Trajectory Line
fig.add_trace(go.Scatter(
    x=all_m,
    y=all_b,
    mode='lines+markers',
    marker=dict(size=8, color='white', symbol='x'),
    line=dict(color='white', width=2),
    name='GD Steps'
))

fig.update_layout(
    title='Gradient Descent Path on 2D Contour Map',
    xaxis_title='Slope (m)',
    yaxis_title='Intercept (b)',
    width=750,
    height=600
)

fig.show()