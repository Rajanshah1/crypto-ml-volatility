from __future__ import annotations
import pandas as pd
from arch import arch_model

def fit_garch(returns: pd.Series, p: int = 1, q: int = 1):
    r = (returns.dropna() * 100)  # percentage returns
    am = arch_model(r, vol="Garch", p=p, q=q, mean="Zero", dist="normal")
    res = am.fit(disp="off")
    return res

def forecast_vol(res, horizon: int = 5) -> pd.DataFrame:
    fc = res.forecast(horizon=horizon, reindex=False)
    var = fc.variance.values[-1]
    vol = (var ** 0.5) / 100.0  # back to return scale
    return pd.DataFrame({"step": range(1, len(vol)+1), "volatility": vol})
