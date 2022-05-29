from typing import final

from numpy import full
from get_data import get_data
import datetime
import pandas as pd
from pprint import pprint

'''gets ful data of the stock '''

# print(today + tdela)

start_dates = pd.date_range(start='2020-02-01',end='2022-05-27',freq='60D')

# gets rid of the time in the date
start_dates_ = start_dates.date
i = 0
while i < len(start_dates_)-1:
  data =get_data('1921537',start_dates_[i],start_dates_[i+1],'day')
  data = data['data']
  candles = data['candles']
  pd_data = pd.DataFrame(candles, columns=['Date','Open','High','Low','Close','volume','None'])
  print(pd_data)
  i += 1
 

def missing_date():
    new_list = []
    length = len(start_dates) 
    final_date = start_dates[length-1].strftime('%Y-%m-%d')
    '''calculate number of missing dates till today '''
    today = str(datetime.date.today())
    data =get_data('1921537',final_date,today,'day')
    data = data['data']
    candles = data['candles']
    pd_data = pd.DataFrame(candles, columns=['Date','Open','High','Low','Close','volume','None'])
    print(pd_data)


# function to store data to a file
def store_candle_data(data,filename):
    with open(f'stocks_data/{filename}','w') as f:
        f.write(data)

missing_date()

