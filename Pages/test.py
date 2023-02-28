import plotly.graph_objs as go

# Example data
x = [1, 2, 3]
y = [4, 5, 6]
name = ['Point A: This is a very long name that needs to be broken into two lines', 'Point B', 'Point C']
description = ['This is Point A', 'This is Point B', 'This is Point C']
customdata = list(zip(name, description))

# Create the trace with hovertemplate
trace = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    customdata=customdata,
    hovertemplate='<b>%{customdata[0]:.40s}</b><br>%{customdata[0]:.40s}<br>%{customdata[1]}'
)

# Create the figure
fig = go.Figure(trace)

# Show the figure
fig.show()
