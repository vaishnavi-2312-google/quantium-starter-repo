import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import datetime

# Load processed data
df = pd.read_csv("output/combined_sales.csv")

# Convert date column to datetime & sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# Create the Dash app
app = Dash(__name__)

# Line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"},
)

# Add a vertical line using SHAPE (safe method)
fig.add_shape(
    type="line",
    x0=datetime.datetime(2021, 1, 15),
    x1=datetime.datetime(2021, 1, 15),
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", width=2, dash="dash")
)

# Optional: Add a label for the price increase
fig.add_annotation(
    x=datetime.datetime(2021, 1, 15),
    y=df['sales'].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=3,
    bgcolor="white"
)

# App layout
app.layout = html.Div(children=[
    html.H1("Soul Foods Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(id="sales-graph", figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)