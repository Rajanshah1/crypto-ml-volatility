#!/usr/bin/env python
import argparse
from pathlib import Path
from src.cryptoml_vol.data.download import fetch_ohlcv
from src.cryptoml_vol.data.preprocess import basic_pipeline
from src.cryptoml_vol.utils.io import save_parquet

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", default="BTC-USD")
    p.add_argument("--start", default="2018-01-01")
    p.add_argument("--end", default=None)
    p.add_argument("--out", default=None, help="Override output parquet path")
    args = p.parse_args()

    df = fetch_ohlcv(args.ticker, args.start, args.end)
    feats = basic_pipeline(df)
    out = args.out or f"processed/{args.ticker}.parquet"
    save_parquet(feats, out)
    print(f"Saved {len(feats):,} rows to data/{out}")

if __name__ == "__main__":
    main()
