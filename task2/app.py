# task2/app.py
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# ---------- Load and normalize ----------
fn = "task2/data/LuxuryLoanPortfolio.csv"
df = pd.read_csv(fn, dtype=str)  # read as strings first to be safe

# normalize column names to snake_case and lower-case
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^0-9a-z]+", "_", regex=True)  # non-alphanumeric -> underscore
    .str.strip("_")
)

# Helpful: show available columns if you need to debug
# print("columns:", list(df.columns))

# ---------- Convert & coerce numeric/date columns ----------
# common numeric candidates in your file
maybe_nums = [
    "funded_amount", "payments", "total_past_payments",
    "loan_balance", "property_value",
    "interest_rate_percent", "interest_rate"
]
for c in maybe_nums:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c].str.replace(',', '').str.strip(), errors="coerce")

# parse funded_date if present
if "funded_date" in df.columns:
    df["funded_date"] = pd.to_datetime(df["funded_date"], errors="coerce")

# ---------- Prepare charts ----------

# 1) Histogram: distribution of funded_amount
if "funded_amount" in df.columns:
    fig_hist = px.histogram(
        df,
        x="funded_amount",
        nbins=50,
        title="Distribution of Funded Amounts",
        labels={"funded_amount": "Funded amount (USD)"},
        hover_data=["loan_id"] if "loan_id" in df.columns else None
    )
else:
    fig_hist = px.histogram(title="No funded_amount column found")

# 2) Scatter: property_value vs funded_amount
scatter_color = "state" if "state" in df.columns else ("purpose" if "purpose" in df.columns else None)
scatter_size = "loan_balance" if "loan_balance" in df.columns else None

if "property_value" in df.columns and "funded_amount" in df.columns:
    fig_scatter = px.scatter(
        df,
        x="property_value",
        y="funded_amount",
        size=scatter_size,
        color=scatter_color,
        hover_data=[c for c in ("loan_id","firstname","lastname") if c in df.columns],
        title="Funded Amount vs Property Value"
    )
else:
    fig_scatter = px.scatter(title="Insufficient columns for scatter (need property_value & funded_amount)")

# 3) Time series: avg funded_amount by year
if "funded_date" in df.columns and df["funded_date"].notna().any():
    df["year"] = df["funded_date"].dt.to_period("Y").dt.to_timestamp()
    trend = df.groupby("year", as_index=False).agg(avg_funded_amount=("funded_amount","mean"))
    fig_time = px.line(
        trend,
        x="year",
        y="avg_funded_amount",
        markers=True,
        title="Average Funded Amount by Year",
        labels={"avg_funded_amount": "Avg Funded Amount", "year": "Year"}
    )
else:
    # fallback: boxplot of funded_amount by state (if no dates)
    if "funded_amount" in df.columns and ("state" in df.columns or "city" in df.columns):
        bycol = "state" if "state" in df.columns else "city"
        fig_time = px.box(df, x=bycol, y="funded_amount", title=f"Funded Amount by {bycol.title()}")
    else:
        fig_time = px.line(title="No date or geographic column available for time series")

# ---------- Build Dash app ----------
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Luxury Loan Portfolio Dashboard"),
    html.P("3 charts: Histogram, Scatter, Time series (or fallback)."),

    html.H3("1. Funded Amount Distribution"),
    dcc.Graph(figure=fig_hist),

    html.H3("2. Funded Amount vs Property Value"),
    dcc.Graph(figure=fig_scatter),

    html.H3("3. Time series / Regional boxplot"),
    dcc.Graph(figure=fig_time),
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
