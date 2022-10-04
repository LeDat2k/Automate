#!/usr/bin/env python3

import sys
import time
import os
import pickle
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# cookie_path = '/media/dat/DISK/Dev/Automation/Shopee/scookies.pkl'
cookie_path = os.path.join(Path(__file__).absolute().parent, 'shopee_cookies.pkl')


def save_cookies():
    driver_service = Service(executable_path="/media/dat/DISK/Dev/Automation/BrowserDrivers/chromedriver")
    driver = webdriver.Firefox(service=driver_service)

    driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")

    username = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input')
    username.send_keys("dat25600")
    password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input')
    password.send_keys("LinD2018")
    password.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button'))
    ).click()

    # wait for 2nd validation
    wait = WebDriverWait(driver, 70)
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/a[1]/div/div[1]/div/div'))
    )

    pickle.dump(driver.get_cookies(), open(cookie_path, "wb"))
    driver.quit()

    cmd = 'notify-send "Saved new cookies!" "Thing is done"'
    os.system(cmd)


def claim_coin():
    try:
        options = Options()
        options.headless = True
        driver_service = Service(executable_path="/media/dat/DISK/Dev/Automation/BrowserDrivers/geckodriver")
        driver = webdriver.Firefox(service=driver_service, options=options)
        driver.get("https://shopee.vn/")

        cookies = pickle.load(open(cookie_path, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://shopee.vn/shopee-coins")

        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/div/div[2]/div/main/section[1]/div[1]/div/section/div[2]/button'))
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input'))
        ).send_keys('dat25600')

        password = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input')
        password.send_keys("LinD2018")
        password.send_keys(Keys.ENTER)

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/div/div[2]/div/main/section[1]/div[1]/div/section/div[2]/button'))
        ).click()

        time.sleep(2)
        driver.quit()

    except:
        error = f"{sys.exc_info()[0]}"
        os.system(f'notify-send "Error" "{error}\nWait 60 seconds"')
        print(error)
        # time.sleep(60)

# save_cookies()
# claim_coin()
