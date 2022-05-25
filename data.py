import requests
from  config import *
from pprint import pprint

url = 'https://kite.zerodha.com/api/login'

main_header = {

'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'content-length': '43',
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

}
session = requests.Session()
response = session.post(url,auth=(USER_NAME,PASSWORD),headers=main_header,cookies=session.cookies)
pprint(response.text)


