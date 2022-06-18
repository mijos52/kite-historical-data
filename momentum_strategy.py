'''
this strategy intends to replicate and backest popular momentum based strageies that give importance to news 
 and also to volume comparison 

#varibles requires

volume - directly from the data
relative_volume_times - today volume/average volume 
gap_percentage - current open is higher than previouse day close / vice versa for low_gaps
week_high - take pandas ta series for week and calculate the highest value of them 
month_high - take month high value of series of data 
52_week_high - 
pivot_points - use tradignview indicator data for construction
day_low - from data
day_high - from data
atr_stock - use inbuilt indictor vectorbt , Ta lib
current_price - fom data 
change_percentage - from data , current price - previous price / 100

# strategy

buying - when relative volume is higher than 2 , close to a pivot point , atr of stock as stoploss , 

stuff to check 
-how nifty is doing
-how sector is doing 
-is there a news in the stock 
- does the voume confirm our thesis 
- is it making some kind of indentifable patterns
- what is the loing term suport and resitsance for the stock 





'''
import pandas as pd
import vectorbt as vbt


# volume from pandas data
stock_data = pd.read_csv('./venv/stocks_data/2815745_day.csv')
stock_volume = stock_data['Volume']


# relative_volume calculation

''' sum of last 21 days volume  by 21 = average volume '''


stock_avg_volume = stock_volume.rolling(21, min_periods=1).sum()/21


print(stock_avg_volume)