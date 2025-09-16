PY=python

setup:
	pip install -r requirements.txt

data:
	$(PY) scripts/prepare_data.py --ticker BTC-USD --start 2018-01-01

app:
	streamlit run src/cryptoml_vol/app/streamlit_app.py

test:
	pytest -q
