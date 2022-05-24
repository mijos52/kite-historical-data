import requests 
from pprint import pprint
from config import*
import json

"""logs into kite zerodha using sessions from requests lib"""

url = 'https://kite.zerodha.com/api/login'
r = requests.get(url)
cookies = r.cookies

session = requests.session()

headers = {

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


result  = session.post('https://kite.zerodha.com/api/login',headers=headers,cookies=cookies,data=pay_load)
result_json = result.json()

request_data = result_json['data']
request_id = request_data['request_id']

print(request_id)


# two-factor authentication
twofa_url = 'https://kite.zerodha.com/api/twofa'
pay_load = {

'user_id': USER_NAME,
'request_id': request_id,
'twofa_value': PIN_NUBMER,
'skip_session': ''

}

# post request for two-factor authentication
result = session.post(twofa_url,headers=headers,cookies=cookies,data =pay_load )
print(result.text)


""""""
