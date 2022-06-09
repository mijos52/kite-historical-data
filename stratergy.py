import vectorbt as vbt
import pandas as pd
import numpy as np

price = pd.read_csv('venv/stocks_data/2815745_day.csv')  
duplicates =  price[price.duplicated()]
print(duplicates)
# price_close_numpy = price['Close'].to_numpy()
# price_open_numpy = price['Open'].to_numpy()
# price_volume_numpy = price['Volume'].to_numpy()

# # pf = vbt.Portfolio.from_holding(price_close_numpy, init_cash=100)
# # print(pf.total_profit())

# # trade data

# fast_ma = vbt.MA.run(price_close_numpy, 10)
# slow_ma = vbt.MA.run(price_close_numpy, 50)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)

# pf = vbt.Portfolio.from_signals(price_close_numpy, entries, exits, init_cash=100)
# print(pf.total_profit())

