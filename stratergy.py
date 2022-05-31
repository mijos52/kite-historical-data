import vectorbt as vbt
import pandas as pd
import numpy as np

price = pd.read_csv('stocks_data/1921537_day.csv')  
price_close_numpy = price['Close'].to_numpy()
price_close = price['Close']


pf = vbt.Portfolio.from_holding(price_close_numpy, init_cash=100)
pf.total_profit()

# # trade data

# fast_ma = vbt.MA.run(price_close, 10)
# slow_ma = vbt.MA.run(price_close, 50)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)

# pf = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100)
# pf.total_profit()
