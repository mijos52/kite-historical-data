from  get_candle_data import  get_data
import datetime
import pandas as pd
import os 
import logging

logging.basicConfig(filename='./venv/logs/logs.txt',level=logging.INFO)

symbol_id = '256265'
time_frame = 'day'

logging.info('programm started ')

def list_of_dates(start_date:str, end_date:str, frequency:str)-> list:
  logging.info('list of dates')
  date_list = pd.date_range(start=start_date,end=end_date,freq=frequency)
  start_dates = date_list.date 
  return start_dates

start_dates_ = list_of_dates(start_date='2022-03-01',end_date='2022-06-18',frequency='60D')


def delete_file(file:str, symbol_id:str, time_frame:str)-> None:

  logging.info('delete files ')

  file = f'venv/stocks_data/{symbol_id}_{time_frame}.csv'
  if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)
    print("file deleted")
  else:
    print("file not found") 
    
    
def save_data(dataframe:pd.DataFrame, symbol_id:str, time_frame:str, mode:str)-> None:
  logging.info('save data ')
  dataframe.to_csv(f'./venv/stocks_data/{symbol_id}_{time_frame}.csv', mode=mode, index=False, header=False)
   

# gets candles data and saves it to a csv
def first_date_candles():
  
  logging.info('first candle data ')
  i = 0
  while i < len(start_dates_)-1:
    data =get_data(symbol_id,start_dates_[i],start_dates_[i+1],time_frame)
    candles = data['data']['candles']
    dataframe = pd.DataFrame(candles)

    save_data(dataframe=dataframe, symbol_id=symbol_id, time_frame=time_frame,mode='a')
    i+=1
 
# gets missing candles data and appends it to csv
def missing_date_candles():
    
    logging.info('missing date candles function  ')

    length = len(start_dates_) 
    start_date = start_dates_[length-1].strftime('%Y-%m-%d')
    end_date = str(datetime.date.today())

    data =get_data(symbol_id,start_date,end_date,time_frame)
    candles = data['data']['candles']
    dataframe = pd.DataFrame(candles)
    save_data(dataframe=dataframe, symbol_id=symbol_id, time_frame=time_frame,mode='a')

''' code to remove the duplicate entries in the dataframe'''
def remove_duplicates():
  
  logging.info('remove duplicates function ')
  price = pd.read_csv(f'venv/stocks_data/{symbol_id}_{time_frame}.csv')  
  price = price.drop_duplicates()
  file = f'venv/stocks_data/{symbol_id}_{time_frame}.csv'
  delete_file(file=file, symbol_id=symbol_id, time_frame=time_frame)

  # assign coloums to the sheets
  column_headers = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume','None'])
  save_data(dataframe=column_headers, symbol_id=symbol_id, time_frame=time_frame,mode='w')
  save_data(dataframe=price, symbol_id=symbol_id, time_frame=time_frame,mode='a')


def main() -> None:
  try:
    
    logging.info('Inside main function ')
    first_date_candles()
    missing_date_candles()
    remove_duplicates()
  except Exception as e:
    print('CHECK WHETHER YOU ARE LOGGED IN TO KITE')
    print(e)

main()