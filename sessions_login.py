from dataclasses import dataclass
import requests 
from pprint import pprint
from config import*
import json

"""logs into kite zerodha using sessions from requests lib"""

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

print(request_id)
print(result.cookies)



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
print(special_cookie)

public_token = ''


#set api preference


#headers

header={

'authority': 'kite.zerodha.com',
'method': 'GET',
'path': '/api/chart/preferences?user_id=AX2602&type=tradingview',
'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'cookie':str(special_cookie),
'referer': 'https://kite.zerodha.com/chart/web/tvc/NSE/BSE/5013761',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
# 'x-csrftoken': 'aBN5Ff389hgyrsXN52XtFKCRK5enkMpe',
'x-kite-userid': 'AX2602',
'x-kite-version': '2.9.11'

}



pay_load = {

'user_id': 'AX2602',
'type': 'tradingview'
}

response = session.get('https://kite.zerodha.com/api/chart/preferences?user_id=AX2602&type=tradingview',cookies=special_cookie,headers=header)
print(response.text)

 
""" data requests """

headers ={


'authority': 'kite.zerodha.com',
'method': 'GET',
'path': '/oms/instruments/historical/987393/day?user_id=AX2602&oi=1&from=2021-11-22&to=2022-05-24',
'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'authorization': enctoken,
'referer': 'https://kite.zerodha.com/chart/ext/tvc/NSE/VARROC/987393',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

 }



pay_load = {
'user_id': 'AX2602',
'oi': '1',
'from': '2021-11-22',
'to': '2022-05-24'
}

response = session.get('https://kite.zerodha.com/oms/instruments/historical/987393/day?user_id=AX2602&oi=1&from=2021-11-22&to=2022-05-24',data=pay_load,headers=headers,cookies=special_cookie,)
print(response.text)


