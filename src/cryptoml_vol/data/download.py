from __future__ import annotations
import pandas as pd
import yfinance as yf
from datetime import datetime

def fetch_ohlcv(ticker: str, start: str = "2018-01-01", end: str | None = None, interval: str = "1d") -> pd.DataFrame:
    end = end or datetime.today().strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, end=end, interval=interval, auto_adjust=False, progress=False)
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise RuntimeError(f"No data returned for {ticker}")
    df["Ticker"] = ticker
    df = df.reset_index().rename(columns={"Date": "Date"})
    return df
