import requests
from pprint import pprint
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

'''calls the api and also currenlty has streamlit'''


def get_data(symbol,from_date,to_date,time_frame):
    session = requests.Session()
    # load all return values from kite_login()

    with open('token.txt','r') as f:
        PRIVATE_TOKEN = f.read()
    
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

    response = requests.get(f'https://kite.zerodha.com/oms/instruments/historical/{symbol}/{time_frame}?user_id=AX2602&oi=1&from={from_date}&to={to_date}',headers=headers,data=pay_load)
    return response.json()



# strealit 
st.header('Dashboard')

#streamlit sidebar 

''''getting input form stramlit for url '''
sidebar = st.sidebar
sidebar.header('Options')
symbol_entry = sidebar.text_input('enter symbol',value='1921537')
time_entry=sidebar.select_slider('Select timeframe',options=['minute', '2minute', '5minute', '15minute', 'day'])
fromdate_entry=sidebar.date_input('from date')
todate_entry=sidebar.date_input('to date')

def on_click():
    try:
        data = get_data(symbol_entry,fromdate_entry,todate_entry,time_entry)

        data = data['data']
        candles = data['candles']

       #assign columns to candles
        candle_pd = pd.DataFrame(candles,columns =['Date','Open','High','Low','Close','Volume','value'])

        candle_close = candle_pd['Open']
        candle_date = candle_pd['Date']
        candle_date = pd.DataFrame(candle_date,)

        st.write(candle_pd)

        date_close_chart = pd.DataFrame(candle_close,candle_date)
        # st.line_chart(date_close_chart) 
    except Exception as e:
        st.write(e)

sidebar.button('Get details',on_click=on_click())