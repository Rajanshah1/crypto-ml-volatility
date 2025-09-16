import numpy as np
import pandas as pd

def rmse(y_true: pd.Series, y_pred: pd.Series) -> float:
    a = y_true.loc[y_pred.index]
    return float(np.sqrt(np.mean((a - y_pred)**2)))

def mape(y_true: pd.Series, y_pred: pd.Series) -> float:
    a = y_true.loc[y_pred.index].replace(0, np.nan)
    return float(np.mean(np.abs((a - y_pred) / a)) * 100)

def var(series: pd.Series, alpha: float = 0.95) -> float:
    return float(np.quantile(series.dropna(), 1 - alpha))

def cvar(series: pd.Series, alpha: float = 0.95) -> float:
    v = var(series, alpha)
    tail = series[series <= v]
    return float(tail.mean())
