import pandas as pd

def sma(df: pd.DataFrame, col: str = "Close", window: int = 20):
    return df[col].rolling(window).mean()

def ema(df: pd.DataFrame, col: str = "Close", span: int = 20):
    return df[col].ewm(span=span, adjust=False).mean()
