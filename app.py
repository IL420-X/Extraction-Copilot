import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="1% Extraction Co-Pilot", page_icon="🚀", layout="wide")

# Custom CSS for nice design
st.markdown("""
<style>
    .main {background-color: #0e1117;}
    .stApp {background-color: #0e1117; color: #ffffff;}
    h1 {color: #00ff9d !important; font-family: 'Helvetica Neue', sans-serif;}
    .stMetric {background-color: #1e242c; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 1% Extraction Co-Pilot")
st.markdown("**Free AI-powered tool for the robotics & AI megacycle** — built live while stacking 500 €/month, hitting MMA, and becoming the Possible Human")

# (rest of your previous code stays exactly the same — just paste the rest from the last working version or tell me "paste the rest" and I'll give it)

# At the very bottom add this nice footer
st.caption("Built live with Grok 4.20 • Your story starts here • Share this tool and help others compound too")
