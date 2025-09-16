from __future__ import annotations
import numpy as np
import pandas as pd
try:
    from hmmlearn.hmm import GaussianHMM
except Exception:
    GaussianHMM = None

def fit_hmm(returns: pd.Series, n_states: int = 2, random_state: int = 42):
    if GaussianHMM is None:
        raise ImportError("hmmlearn is not installed. Please install hmmlearn to use HMM regimes.")
    r = returns.dropna().values.reshape(-1, 1)
    model = GaussianHMM(n_components=n_states, covariance_type="full", n_iter=200, random_state=random_state)
    model.fit(r)
    states = model.predict(r)
    idx = returns.dropna().index
    return pd.Series(states, index=idx, name="Regime")
