import functools

import requests

# v_content_url = "https://virgool.io/@mahsa.tabrizi92/%D9%81%D8%B1%DB%8C%D9%85%D9%88%D8%B1%DA%A9-%D8%AC%D9%86%DA%AF%D9%88-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%B1%D8%A7-%D8%A7%D8%B2-%DA%A9%D8%AC%D8%A7-%DB%8C%D8%A7%D8%AF-%D8%A8%DA%AF%DB%8C%D8%B1%D9%85-fm9tswkgfrob"

# You can go to network and get Curl and convert it to python code to break the limits!
# v_content_url = "https://www.tsetmc.com/instInfo/35425587644337450" 403
# https://curlconverter.com/


# response = requests.get(v_content_url)
#
# with open("v.html", "wb") as f:
#     f.write(response.content)


# You can go to network and get Curl and convert it to python code to break the limits!
# For other website you can use proxy!

# Proxy setup from MrYazdan's github

# response = requests.get("https://www.navasan.net/dayRates.php?item=usd")
# print(response.status_code)
#
# with open("navasan.html", "wb") as f:
#     f.write(response.content)

# seleniummmm

from selenium import webdriver
from selenium.webdriver.common.by import By
#
from time import sleep

browser = webdriver.Chrome()
# browser.get("https://www.tsetmc.com/instInfo/35425587644337450")
#
# sleep(8)
# # Run this in your browser(css selecotr or maybe xpath(which is slower))
# el = browser.find_element(By.CSS_SELECTOR, "#d02 > div > div")
#
# # el.find_element ???? ---> By.CSS_SELECTOR
# browser.execute_script("arguments[0].innerHTML = '';", el.find_element(By.CSS_SELECTOR, 'span'))
# print(el.text)
# sleep(100)

# You can use in-decorators to deal with the load problem.

# Phase 2
# Movments with Selenium ()
browser.get('https://www.tsetmc.com')
browser.find_element(By.CSS_SELECTOR, '#search').click()

search_inp = browser.find_element(By.CSS_SELECTOR,'input[name="search"]')

user_inp = input("Please enter S.th. \n")
sleep(1)

browser.find_element(By.CSS_SELECTOR, '.jss1 div[ref="eBodyViewport"] .ag-center-cols-clipper .ag-').click()

search_inp.send_keys(user_inp)

