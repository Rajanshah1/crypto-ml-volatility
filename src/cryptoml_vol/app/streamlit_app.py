import os
import pandas as pd
import streamlit as st

from ..utils.plotting import candle
from ..data.preprocess import basic_pipeline
from ..risk.var_cvar import var, cvar

st.set_page_config(page_title="CryptoML-Volatility", layout="wide")
st.title("🧪 CryptoML-Volatility — Starter App")

st.sidebar.header("Data")
source = st.sidebar.selectbox("Source", ["sample", "yfinance"], index=0)
ticker = st.sidebar.text_input("Ticker", "BTC-USD")
lookback_days = st.sidebar.number_input("Lookback (days)", min_value=60, value=365, step=30)

@st.cache_data
def load_sample():
    return pd.read_csv("data/sample/BTC-USD_sample.csv", parse_dates=["Date"])

def load_data():
    if source == "sample":
        df = load_sample()
        return df[df["Ticker"] == "BTC-USD"]
    else:
        from ..data.download import fetch_ohlcv
        df = fetch_ohlcv(ticker=ticker, start="2018-01-01")
        return df

df = load_data().sort_values("Date").tail(lookback_days)

tabs = st.tabs(["Overview", "Volatility", "Risk & Regimes"])

with tabs[0]:
    st.subheader(f"Price — {ticker}")
    st.plotly_chart(candle(df), use_container_width=True)
    st.dataframe(df.tail(10), use_container_width=True)

with tabs[1]:
    st.subheader("Realized Volatility (Rolling 30d) & ATR")
    from ..data.preprocess import basic_pipeline
    feats = basic_pipeline(df)
    st.line_chart(feats.set_index("Date")[["Vol_Rolling","ATR"]])
    st.caption("Vol_Rolling is annualized std of daily returns over a 30-day window. ATR is 14-day Average True Range.")

with tabs[2]:
    st.subheader("Simple Risk: VaR / CVaR (95%) on Daily Returns")
    feats = basic_pipeline(df)
    r = feats["Return"]
    st.write({
        "VaR (95%)": round(var(r, 0.95), 4),
        "CVaR (95%)": round(cvar(r, 0.95), 4),
        "Mean return": round(r.mean(), 6),
        "Std return": round(r.std(), 6)
    })
    st.line_chart(r.set_axis(feats["Date"]))
    st.caption("Negative values indicate losses. VaR/CVaR computed on daily return distribution.")
