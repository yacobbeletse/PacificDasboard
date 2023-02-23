import plotly.graph_objects as go
import pandas as pd
import numpy as np

# create sample data
df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 
                   'category': ['X', 'Y', 'X', 'Y'], 
                   'value': [1, 2, 3, 4]})

# define the angles for each group
angles = np.linspace(0, 360, len(df['group'].unique()) + 1)[:-1]

# create a trace for each group
traces = []
for i, group in enumerate(df['group'].unique()):
    group_df = df[df['group'] == group]
    # define the angles for each category within the group
    theta = angles[i] + np.linspace(0, 360/len(group_df), len(group_df) + 1)[:-1]
    trace = go.Barpolar(r=group_df['value'], 
                        theta=theta, 
                        name=group, 
                        marker_color=i)
    traces.append(trace)

# create the layout
layout = go.Layout(polar={'angularaxis': {'direction': 'clockwise'},
                           'radialaxis': {'range': [0, 5]}},
                   barmode='group')

# create the figure and plot it
fig = go.Figure(data=traces, layout=layout)
fig.show()