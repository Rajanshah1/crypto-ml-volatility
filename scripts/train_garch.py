#!/usr/bin/env python
import argparse, pickle, os
from src.cryptoml_vol.utils.io import load_parquet
from src.cryptoml_vol.models.garch import fit_garch, forecast_vol

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="data/processed/*.parquet")
    p.add_argument("--out", default="outputs/garch_model.pkl")
    p.add_argument("--horizon", type=int, default=5)
    args = p.parse_args()

    df = load_parquet(args.input)
    res = fit_garch(df["Return"])
    fc = forecast_vol(res, args.horizon)
    print("Volatility forecast:\n", fc)

    os.makedirs("outputs", exist_ok=True)
    with open(args.out, "wb") as f:
        pickle.dump(res, f)
    print(f"Saved model to {args.out}")

if __name__ == "__main__":
    main()
