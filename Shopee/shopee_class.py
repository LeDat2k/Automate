#!/usr/bin/env python3
import os, time, pickle, sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Shopee:
    def __init__(self, cookies_path, driver_path) -> None:
        self.cookie_path = os.path.join(Path(__file__).absolute().parent, 'shopee_cookies.pkl')
        self.driver_path = "/media/dat/DISK/Dev/Automation/BrowserDrivers/chromedriver"

    def save_cookies(self):
        driver_service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=driver_service)
        driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")
        time.sleep(10)
        driver.quit()



dat = Shopee()
dat.save_cookies()