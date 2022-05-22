import requests
from config import*

url = 'https://kite.zerodha.com/api/login'
r = requests.get(url)
cookies = r.cookies

headers = {

# 'authority': 'kite.zerodha.com',
# 'method': 'POST',
# 'path': '/api/login',
# 'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'content-length': '43',
'content-type': 'application/x-www-form-urlencoded',
# 'origin': 'https://kite.zerodha.com',
# 'referer': 'https://kite.zerodha.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': "Windows",
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
# 'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

}

pay_load = {

'user_id': USER_NAME,
'password': PASSWORD

}


result  = requests.post('https://kite.zerodha.com/api/login',headers=headers,cookies=cookies,data=pay_load)
print(result.elapsed)

# two-factor authentication
twofa_url = 'https://kite.zerodha.com/api/twofa'
pay_load = {

'user_id': 'AX2602',
'request_id': 'ihqUVNNlVywbZqytma8Am5t0IRvnB6ulIh17Zu66wGkP3RljwUH63UQRRFoot4Wq',
'twofa_value': '199696',
'skip_session': ''


}

result = requests.post(twofa_url,headers=headers,cookies=cookies,data =pay_load )
print(result)