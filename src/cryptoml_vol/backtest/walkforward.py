from __future__ import annotations
import pandas as pd
from typing import Callable

def walk_forward(series: pd.Series, train_size: int, step_fn: Callable):
    """
    For each step after `train_size`, fit on the past and predict the next step.
    step_fn takes (train_series) -> prediction_for_next_step (float).
    """
    preds, idxs = [], []
    for i in range(train_size, len(series)-1):
        train = series.iloc[:i]
        pred = step_fn(train)
        preds.append(pred)
        idxs.append(series.index[i+1])
    return pd.Series(preds, index=idxs)
