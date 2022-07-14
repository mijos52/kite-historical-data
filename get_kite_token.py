import config
import requests

"""Gets authentication token for kite api and stores in a token.txt file """

def kite_login() -> str:

    result  = requests.post(url=config.KITE_LOGIN_URL, headers=config.HTTP_HEADER, data=config.LOGIN_PAY_LOAD)
    result_json = result.json()

    request_id = result_json['data']['request_id']
    return request_id


pay_load:dict = {

    'user_id': config.USER_NAME,
    'request_id': kite_login(),
    'twofa_value': config.PIN_NUMBER,
    'skip_session': ''

    }


def kite_two_factor_authentication() -> str:

    result = requests.post(url=config.KITE_TWO_FACTOR_LOGIN_URL,headers=config.HTTP_HEADER, data =pay_load )
    special_cookie = result.cookies
    private_token = special_cookie['enctoken']

    return private_token


def save_token(private_token) -> None:
    print(f'logged in private token is {private_token} ')
    with open('token.txt','w') as f:
        f.write(private_token)

def main() -> None:
    private_token = kite_two_factor_authentication()
    save_token(private_token=private_token)


if __name__ =="__main__":
    main()