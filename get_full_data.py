from get_data import get_data
import datetime
import pandas as pd
import os 

# get all dates with freq of 60 Days
start_dates = pd.date_range(start='2021-01-01',end='2022-06-01',freq='60D')

# remove time format and make it date only in str format
start_dates_ = start_dates.date

#global variables for functions
symbol_id = '2815745'
time_frame = 'day'

file = f'venv/stocks_data/{symbol_id}_{time_frame}.csv'
if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)
  print("file deleted")
else:
  print("file not found")

  # assign coloums to the sheets
column_name = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume','None'])
column_name.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode='w', index=False)


# gets candles data and saves it to a csv
def first_date_candles():
  i = 0
  while i < len(start_dates_)-1:
    data =get_data(f'{symbol_id}',start_dates_[i],start_dates_[i+1],f'{time_frame}')
    data = data['data']
    candles = data['candles']
    pd_data_1 = pd.DataFrame(candles)
    pd_data_1.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode='a', index=False, header=False)
    i+=1
 
# gets missing candles data and appends it to csv
def missing_date_candles():
    new_list = []
    length = len(start_dates) 
    final_date = start_dates[length-1].strftime('%Y-%m-%d')
    today = str(datetime.date.today())
    data =get_data(f'{symbol_id}',final_date,today,f'{time_frame}')
    data = data['data']
    candles = data['candles']
    pd_data_2 = pd.DataFrame(candles)
    pd_data_2.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode='a', index=False, header=False)

''' code to remove the duplicate entries in the dataframe'''
def remove_duplicates():
  price = pd.read_csv(f'venv/stocks_data/{symbol_id}_{time_frame}.csv')  
  price.drop_duplicates(subset=['Date'])
  file = f'venv/stocks_data/{symbol_id}_{time_frame}.csv'
  if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)
    print("file deleted")
  else:
    print("file not found")
  # assign coloums to the sheets
  column_name = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume','None'])
  column_name.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode='w', index=False)
  price.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode='a', index=False, header=False)


try :
  first_date_candles()
  missing_date_candles()
except Exception as e:
  print('CHECK WHETHER YOU ARE LOGGED IN TO KITE')
  print(e)

remove_duplicates()