from __future__ import annotations
import pandas as pd
from pathlib import Path
import os

DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))

def save_parquet(df: pd.DataFrame, path: str):
    p = DATA_DIR / path
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(p, index=False)

def load_parquet(path: str) -> pd.DataFrame:
    p = DATA_DIR / path
    return pd.read_parquet(p)
