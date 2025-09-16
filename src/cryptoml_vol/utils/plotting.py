import plotly.graph_objects as go
import pandas as pd

def candle(df: pd.DataFrame):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'])])
    fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), height=420)
    return fig
