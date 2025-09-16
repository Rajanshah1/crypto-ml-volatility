import pandas as pd
import numpy as np

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Return"] = df["Adj Close"].pct_change()
    return df

def rolling_volatility(df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    df = df.copy()
    df["Vol_Rolling"] = df["Return"].rolling(window).std() * np.sqrt(252)
    return df

def atr(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    df = df.copy()
    high_low = (df["High"] - df["Low"]).abs()
    high_close = (df["High"] - df["Close"].shift()).abs()
    low_close = (df["Low"] - df["Close"].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df["ATR"] = tr.rolling(window).mean()
    return df

def basic_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = compute_returns(df)
    df = rolling_volatility(df, 30)
    df = atr(df, 14)
    return df.dropna().reset_index(drop=True)
