import plotly.graph_objects as go
import pandas as pd

# Create some data for the chart
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 3, 2, 4, 3]
})

# Create a line chart
fig = go.Figure()

# Add a trace for the upper filled area
fig.add_trace(
    go.Scatter(
        x=[1,5], y=[2,2], mode='lines', line_color='rgba(0, 176, 246, 1)',
        fill='tozeroy', fillcolor='rgba(0, 176, 246, 0.2)'
    )
)

# Add a trace for the lower filled area
fig.add_trace(
    go.Scatter(
        x=[1,5], y=[4,4], mode='lines', line_color='rgba(255, 178, 0, 1)',
        fill='tonexty', fillcolor='rgba(255, 178, 0, 0.2)'
    )
)

# Add a trace for the line
fig.add_trace(
    go.Scatter(
        x=[1, 5], y=[2.5, 2.5], mode='lines', line_color='rgba(0, 0, 0, 1)',
        line_width=2
    )
)

# Show the chart
fig.show()
