import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import datetime

# Load processed data
df = pd.read_csv("output/combined_sales.csv")

# Convert date column to datetime & sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# Create the Dash app
app = Dash(__name__)

# --------------------------------------------------
#  LAYOUT
# --------------------------------------------------

app.layout = html.Div(style={
    "backgroundColor": "#f5f5f5",
    "padding": "20px",
    "fontFamily": "Arial"
}, children=[

    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center", "color": "#d6336c"}
    ),

    html.Div([
        html.Label("Filter by Region:", style={"fontSize": "20px", "fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            inline=True,
            style={"marginTop": "10px", "marginBottom": "25px"}
        )
    ]),

    dcc.Graph(id="sales-graph")
])

# --------------------------------------------------
#  CALLBACK
# --------------------------------------------------

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    # Filter the data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create line plot
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.upper()})",
        labels={"date": "Date", "sales": "Total Sales"},
    )

    # Add vertical price-change line
    fig.add_vline(
        x=datetime.datetime(2021, 1, 15),
        line_width=2,
        line_dash="dash",
        line_color="red"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f5f5f5",
        title_font_size=24
    )

    return fig

# --------------------------------------------------
#  RUN SERVER
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)