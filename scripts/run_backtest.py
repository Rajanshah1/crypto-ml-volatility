#!/usr/bin/env python
import argparse
import numpy as np
from src.cryptoml_vol.utils.io import load_parquet
from src.cryptoml_vol.backtest.walkforward import walk_forward
from src.cryptoml_vol.backtest.metrics import rmse, mape

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--train-size", type=int, default=200)
    args = p.parse_args()

    df = load_parquet(args.input)
    series = df["Return"]

    # naive model: predict next return as mean of last 30 days
    def step_fn(train):
        return float(np.mean(train[-30:]))

    preds = walk_forward(series, train_size=args.train_size, step_fn=step_fn)
    y_true = series.loc[preds.index]
    print("RMSE:", rmse(y_true, preds))
    print("MAPE:", mape(y_true.clip(lower=1e-6), preds))

if __name__ == "__main__":
    main()
