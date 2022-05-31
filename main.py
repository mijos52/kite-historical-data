import requests 
from pprint import pprint
from config import*

"""logs into kite zerodha using sessions from requests lib
2 login urls are used for authentication and api url to access the data
login urls use the same header but api use different header with all necessary tokens which acts as api_keys

"""
def main():
    url = 'https://kite.zerodha.com/api/login'
    r = requests.get(url)
    cookies = r.cookies

    session = requests.Session()

    main_header = {

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
    kf_session =result.cookies['kf_session']

    enctoken = 'enctoken'+' '+request_id

    # two-factor authentication
    twofa_url = 'https://kite.zerodha.com/api/twofa'
    pay_load = {

    'user_id': USER_NAME,
    'request_id': request_id,
    'twofa_value': PIN_NUMBER,
    'skip_session': ''

    }

    # post request for two-factor authentication
    result = session.post(twofa_url,headers=main_header,cookies=cookies,data =pay_load )
    special_cookie = result.cookies

    # values for all tokens
    
    public_token =special_cookie['public_token']
    private_token = special_cookie['enctoken']

    print(f'logged in private token is {private_token} ')
    with open('token.txt','w') as f:
        f.write(private_token)

main()