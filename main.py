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


app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Analysis"
    ),
    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
