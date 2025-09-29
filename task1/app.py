import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df_product = pd.read_csv("task1/data/avg_by_product.csv")
df_server = pd.read_csv("task1/data/avg_by_server.csv")
df_month = pd.read_csv("task1/data/avg_by_month.csv")
df_month["month"] = pd.to_datetime(df_month["month"])

# Create app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("📊 Complaint Resolution Dashboard"),

    html.H2("Average Resolution by Product"),
    dcc.Graph(
        figure=px.bar(
            df_product.sort_values("avg_resolution_days"),
            x="avg_resolution_days",
            y="product",
            orientation="h",
            text="total_complaints",
            title="Average Resolution Days by Product"
        )
    ),

    html.H2("Monthly Trend of Resolution Time"),
    dcc.Graph(
        figure=px.line(
            df_month,
            x="month",
            y="avg_resolution_days",
            markers=True,
            title="Monthly Resolution Trend"
        )
    ),

    html.H2("Average Resolution by Server"),
    dcc.Graph(
        figure=px.bar(
            df_server.sort_values("avg_resolution_days", ascending=False),
            x="server",
            y="avg_resolution_days",
            text="complaints_handled",
            title="Average Resolution Days by Server"
        )
    )
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
