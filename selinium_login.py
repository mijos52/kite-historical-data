from email import header
from selenium import webdriver
import requests 
from config import *
import json
import time

"""users selinium driver to login to kite zerodha """

# selinium 
url = "https://kite.zerodha.com/"
driver = webdriver.Chrome()
driver.get(url)

# input user name and password in the text fields
username_input = driver.find_element_by_xpath('//*[@id="userid"]')
username_input.send_keys(USER_NAME)
password_input = driver.find_element_by_xpath('//*[@id="password"]')
password_input.send_keys(PASSWORD)

# submit username and password
submit_button = driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[4]/button')
submit_button.click()

time.sleep(3)

# two factor authentication 
twofa_input= driver.find_element_by_xpath('//*[@id="pin"]')
twofa_input.send_keys(PIN_NUBMER)
twofa_submit = driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[3]/button')
twofa_submit.click()

time.sleep(3)

headers  = {

'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,es;q=0.9',
'content-length': '43',
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
'authorization':'nlsErfeSlzhQOg2DwLkyZvj7E1CtITBLmJUhoKqdf5OhD+4aJKoU5jDWcv9iua7sKSQYfuNWo1fOw6QMnrdduUwEPLlXiSTLMaFxzp/bfuyGseL0G4wG2g=='
}

# response = requests.get(url)
# print(response.headers)

# response = requests.get('https://kite.zerodha.com/oms/instruments/historical/189185/day?user_id=AX2602&oi=1&from=2021-05-22&to=2021-11-21',headers=headers)
# print(response.json())

response = driver.get('https://kite.zerodha.com/chart/ext/tvc/NSE/WIPRO/969473')
print(response)
