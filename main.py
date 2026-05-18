from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_output.csv")

app = Dash(__name__)

df['Date'] = pd.to_datetime(df["Date"])

daily_sales = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

daily_sales = daily_sales.sort_values("Date")

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

fig.add_vline(
    x="2021-01-15",
    line_dash="dash"
    )

fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#f4f6f7",
    title_x=0.5
)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Analysis",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "marginBottom": "10px"
        }
    ),

    html.P(
        "Visualising sales trends before and after the January 15, 2021 price increase.",
        style={
            "textAlign": "center",
            "color": "#7f8c8d",
            "marginBottom": "30px"
        }
    ),

    dcc.Graph(
        figure=fig,
        style={
            "borderRadius": "10px",
            "boxShadow": "0px 4px 10px rgba(0,0,0,0.1)"
        }
    )

], style={
    "backgroundColor": "#f4f6f7",
    "padding": "40px",
    "fontFamily": "Arial"
})

if __name__ == "__main__":
    app.run(debug=True)
