# CryptoML-Volatility — End-to-End Starter

A complete, **runnable** starter for crypto time-series **volatility modeling** with:
- Streamlit app (candlestick, realized vol, ATR, VaR/CVaR, optional regimes)
- GARCH(1,1) modeling via `arch`
- Simple walk-forward backtest scaffold
- Clean project structure + Makefile + Dockerfile + tests

### Quick Start

```bash
# 1) Create & activate virtual env
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) (Optional) Configure
cp .env.example .env

# 4) Launch Streamlit app
streamlit run src/cryptoml_vol/app/streamlit_app.py
```

The app defaults to **sample BTC data** included in `data/sample/`. Switch to "yfinance" in the sidebar to fetch fresh OHLCV by ticker.

### CLI Examples

```bash
# Download & preprocess data
python scripts/prepare_data.py --ticker BTC-USD --start 2020-01-01

# Train GARCH(1,1) on returns and forecast 5 steps
python scripts/train_garch.py --input data/processed/BTC-USD.parquet --out outputs/garch_btc.pkl --horizon 5

# Run a toy walk-forward (mean-of-last-30d) backtest
python scripts/run_backtest.py --input data/processed/BTC-USD.parquet --train-size 200
```

### Make Targets
```bash
make setup   # pip install -r requirements.txt
make data    # default data pipeline (BTC-USD since 2018)
make app     # run Streamlit
make test    # pytest -q
```

### Notes
- `hmmlearn` and `prophet` are **optional**; code checks for presence. If you don’t need them, remove from `requirements.txt`.
- For production trading, add: robust data QA, slippage/fees, execution logic, risk limits, monitoring, etc.

---

© You — MIT or Apache-2.0, your choice.
