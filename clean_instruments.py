import pandas as pd



data = pd.read_csv('instruments.csv')

data_clean = data.drop(['exchange_token', 'last_price','expiry','strike','tick_size','lot_size'], axis=1)
data_clean_ = data_clean[(data_clean.exchange=='NSE' ) & (data_clean.instrument_type=='EQ')]
data_clean_.to_csv('clean_data.csv')
