from __future__ import annotations
import pandas as pd
try:
    from prophet import Prophet
except Exception:
    Prophet = None

def prophet_forecast(df: pd.DataFrame, periods: int = 30):
    if Prophet is None:
        raise ImportError("prophet is not installed. `pip install prophet` to enable forecasts.")
    model_df = df.rename(columns={"Date":"ds", "Adj Close":"y"})[["ds","y"]]
    m = Prophet(daily_seasonality=True)
    m.fit(model_df)
    future = m.make_future_dataframe(periods=periods)
    fc = m.predict(future)
    return fc[["ds","yhat","yhat_lower","yhat_upper"]]
