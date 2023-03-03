import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
# Create dummy dataframes
df1 = pd.DataFrame({'category': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'category': ['E', 'F', 'G', 'H'], 'value': [5, 6, 7, 8]})
df3 = pd.DataFrame({'category': ['I', 'J', 'K', 'L'], 'value': [9, 10, 11, 12]})
df4 = pd.DataFrame({'category': ['M', 'N', 'O', 'P'], 'value': [13, 14, 15, 16]})

# Create the subplots
fig =make_subplots(
    rows=2, cols=2,
    subplot_titles=('Subplot 1', 'Subplot 2', 'Subplot 3', 'Subplot 4'),
    specs=[[{'type': 'barpolar'}]*2]*2
)

# Add the traces to the subplots
fig.add_trace(px.bar_polar(df1, r='value', theta='category').data[0], row=1, col=1)
fig.add_trace(px.bar_polar(df2, r='value', theta='category').data[0], row=1, col=2)
fig.add_trace(px.bar_polar(df3, r='value', theta='category').data[0], row=2, col=1)
fig.add_trace(px.bar_polar(df4, r='value', theta='category').data[0], row=2, col=2)

# Update the layout
fig.update_layout(title='Polar Bar Subplots')

# Show the plot
fig.show()
