import requests
from pprint import pprint

from config import PRIVATE_TOKEN


def get_data(from_date,to_date,time_frame):
    session = requests.Session()
    # load all return values from kite_login()
    
    PRIVATE_TOKEN = 'MdN7teQZRnkIuXHD6rxk82KIeu46Grq5C0qjkcH89TaVVcJyTvk2prxoPSHUu2LwVjc3QruopXVF/Lh3GsFH4MDLMUVI8/TrXDB9jxEfegOPTF3UB1/lZw== '

    headers ={

    'authorization': f'enctoken {PRIVATE_TOKEN}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    pay_load = {

    'user_id': 'AX2602',
    'oi': '1',
    'from': from_date,
    'to': to_date
    }

    response = requests.get(f'https://kite.zerodha.com/oms/instruments/historical/189185/{time_frame}?user_id=AX2602&oi=1&from={from_date}&to={to_date}',headers=headers,data=pay_load)
    pprint(response.text)

get_data('2015-05-25','2015-05-26','15minute')