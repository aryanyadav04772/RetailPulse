import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_retail.csv")

daily_sales = (
    df.groupby("InvoiceDate")["Sales"]
    .sum()
    .reset_index()
)

daily_sales["InvoiceDate"] = pd.to_datetime(
    daily_sales["InvoiceDate"]
)

st.title("Demand Forecasting")

fig = px.line(
    daily_sales,
    x="InvoiceDate",
    y="Sales",
    title="Daily Sales Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)