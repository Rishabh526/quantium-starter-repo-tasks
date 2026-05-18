import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


df = pd.read_csv("formatted_output.csv")

df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Analysis",
        id="header",
        style={
            "textAlign": "center",
            "color": "#2c3e50"
        }
    ),

    html.P(
        "Analyse sales trends before and after the January 15, 2021 price increase",
        id="description",
        style={
            "textAlign": "center",
            "marginBottom": "20px"
        }
    ),

    html.Label(
        "Select Region:",
        id="region-label",
        style={"fontWeight": "bold"}
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label":"All","value":"all"},
            {"label":"North","value":"north"},
            {"label":"East","value":"east"},
            {"label":"South","value":"south"},
            {"label":"West","value":"west"},
        ],
        value="all",
        inline=True,
        style={
            "marginBottom":"25px"
        }
    ),

    dcc.Graph(
        id="sales-graph"
    )

], style={
    "padding":"40px",
    "backgroundColor":"#f4f6f7",
    "fontFamily":"Arial"
})


@app.callback(
    Output("sales-graph","figure"),
    Input("region-filter","value")
)
def update_graph(selected_region):

    filtered_df = df

    if selected_region != "all":
        filtered_df = df[
            df["Region"].str.lower() == selected_region
        ]

    daily_sales = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Sales Trend ({selected_region.capitalize()})",
        labels={
            "Date":"Date",
            "Sales":"Total Sales"
        }
    )

    fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=daily_sales["Sales"].max(),
    line=dict(
        dash="dash",
        width=2
    )
)

    fig.add_annotation(
        x="2021-01-15",
        y=daily_sales["Sales"].max(),
        text="Price Increase",
        showarrow=True
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f7",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)