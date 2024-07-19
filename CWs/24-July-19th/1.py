import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import ActionChains

import pprint
from time import sleep
import urllib.request


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


browser = webdriver.Chrome()
browser.get('https://imgur.com/')
browser.find_element(By.CSS_SELECTOR, '.Searchbar').click()
send_input = browser.find_element(By.CSS_SELECTOR, 'input[name="q"]')
user_input = input('Enter your item name: ')
send_input.send_keys(user_input)
browser.find_element(By.CSS_SELECTOR, '.Searchbar-submitInput').click()

count = 0
while True:
    pages = browser.find_elements(By.CSS_SELECTOR, '.cards > div > a')

    if count >= len(pages):
        break

    pg = pages[count]
    pg.click()
    try:
        count += 1
        container = browser.find_element(By.CSS_SELECTOR, '.imageContainer > img')
        print("First select!")

        sleep(2)
        browser.find_element(By.CSS_SELECTOR, '.Gallery-OptionsMenu > .Dropdown-title').click()
        print("Second select!")

        sleep(2)
        browser.find_element(By.CSS_SELECTOR,
                             '.Gallery-OptionsMenu > .Dropdown-title + .Dropdown-menu--top > .Dropdown-list > :nth-child(2)').click()
        print("Third select!")

        # actionChain = ActionChains(browser)
        # actionChain.context_click(elem).perform()

        url = container.get_attribute('src')
        print(url)


    except NoSuchElementException:
        print("This is vid not a pic \n")

    browser.back()

    """
    if url:
        # Download the image
        image_url = requests.get(url)
        save_as = f"image{count}.jpg"
        count += 1
        download_image(image_url, save_as)
        print(f"Downloaded {url}")

        """

# Slection


#
