import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="1% Extraction Co-Pilot", page_icon="🚀", layout="wide")

st.title("🚀 1% Extraction Co-Pilot")
st.markdown("**Free AI-powered tool for the robotics & AI megacycle** — built live while stacking 500 €/month, hitting MMA, and becoming the Possible Human")

currency = st.sidebar.selectbox("Display currency", ["EUR", "USD"])
eur_usd_rate = yf.Ticker("EURUSD=X").history(period="1d")['Close'].iloc[-1]

st.sidebar.header("Your Portfolio")
tickers = st.sidebar.text_input("Tickers (comma separated)", "TSLA,NVDA,TSM,PLTR,MSTR").upper().split(",")
shares = {}
for t in [t.strip() for t in tickers if t.strip()]:
    shares[t] = st.sidebar.number_input(f"Shares of {t}", value=5.0, step=0.1, key=t)

monthly_eur = st.sidebar.number_input("Monthly addition (€)", value=500, step=50)
years = st.sidebar.slider("Project to how many years?", 5, 40, 20)

# Fetch data
data = {}
total_usd = 0.0
for t in shares:
    stock = yf.Ticker(t)
    price_usd = stock.history(period="1d")['Close'].iloc[-1]
    value_usd = price_usd * shares[t]
    total_usd += value_usd
    data[t] = {"Price": round(price_usd, 2), "Value": round(value_usd, 2)}

df = pd.DataFrame.from_dict(data, orient="index")

# Currency conversion
if currency == "EUR":
    total_value = total_usd / eur_usd_rate
    df["Price"] = df["Price"] / eur_usd_rate
    df["Value"] = df["Value"] / eur_usd_rate
else:
    total_value = total_usd

st.subheader(f"Current Portfolio ({currency})")
st.dataframe(df, use_container_width=True)
st.metric(f"Total Value ({currency})", f"{currency} {total_value:,.2f}")

# Simple projection chart
st.subheader(f"Projected Growth (20% annual assumption)")
future = total_usd
monthly = monthly_eur * eur_usd_rate if currency == "USD" else monthly_eur
for _ in range(years * 12):
    future = future * (1 + 0.20 / 12) + monthly
proj_value = future / eur_usd_rate if currency == "EUR" else future
st.success(f"**In {years} years: {currency} {proj_value:,.0f}**")

st.caption("Built live with Grok 4.20 on Linux • Completely free • Your story starts here")
