import requests 
from pprint import pprint
from config import*

"""logs into kite zerodha using sessions from requests lib
2 login urls are used for authentication and api url to access the data
login urls use the same header but api use different header with all necessary tokens which acts as api_keys

"""

url = 'https://kite.zerodha.com/api/login'
r = requests.get(url)
cookies = r.cookies

session = requests.Session()

main_header = {

'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'content-length': '43',
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

}

pay_load = {

'user_id': USER_NAME,
'password': PASSWORD

}


result  = session.post('https://kite.zerodha.com/api/login',headers=main_header,cookies=cookies,data=pay_load)
result_json = result.json()

request_data = result_json['data']
request_id = request_data['request_id']

enctoken = 'enctoken'+' '+request_id

# two-factor authentication
twofa_url = 'https://kite.zerodha.com/api/twofa'
pay_load = {

'user_id': USER_NAME,
'request_id': request_id,
'twofa_value': PIN_NUBMER,
'skip_session': ''

}

# post request for two-factor authentication
result = session.post(twofa_url,headers=main_header,cookies=cookies,data =pay_load )
special_cookie = result.cookies

# values for all tokens
kf_session =result.cookies['kf_session']
public_token =special_cookie['public_token']
private_token = special_cookie['enctoken']

""" data requests code for kite historical data api  """

headers ={

'authority': 'kite.zerodha.com',
'method': 'GET',
'path': '/oms/instruments/historical/189185/minute?user_id=AX2602&oi=1&from=2022-05-11&to=2022-05-26',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'authorization': f'enctoken {private_token}',
'cookie': f'kf_session={kf_session}; user_id=AX2602; public_token={public_token}; enctoken={private_token}',
'referer': 'https://kite.zerodha.com/static/build/chart.html?v=2.9.11',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
 }

# url inputs
from_date ='2015-05-25'
to_date = '2015-05-26'

pay_load = {

'user_id': 'AX2602',
'oi': '1',
'from': from_date,
'to': to_date
 }

response = session.get(f'https://kite.zerodha.com/oms/instruments/historical/189185/15minute?user_id=AX2602&oi=1&from={from_date}&to={to_date}',headers=headers,cookies=special_cookie,data=pay_load)
print(response.text)


