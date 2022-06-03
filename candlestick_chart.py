import plotly.graph_objects as go
import  pandas as pd

df = pd.read_csv('./venv/stocks_data/1921537_day.csv')


df['Date'] = pd.to_datetime(df['Date'])

fig = go.Figure(data =[go.Candlestick(x = df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])

fig.show()