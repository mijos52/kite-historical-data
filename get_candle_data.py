import requests
import pandas as pd
import config


def read_token() -> str:
     with open('token.txt','r') as file:
        token = file.read()
        return token

PRIVATE_TOKEN = read_token()
headers ={

    'authorization': f'enctoken {PRIVATE_TOKEN}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/101.0.4951.67 Safari/537.36'
    }

def get_data(symbol:str, from_date:str, to_date:str ,time_frame:str) -> dict:
    pay_load = {

    'user_id': ' ',
    'oi': '1',
    'from': from_date,
    'to': to_date
    }

    api_url = f'https://kite.zerodha.com/oms/instruments/historical/{symbol}/{time_frame}?user_id={config.USER_NAME}&oi=1&from={from_date}&to={to_date}'

    response = requests.get(url = api_url, headers=headers, data=pay_load)
    return response.json()
