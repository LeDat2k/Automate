#!/usr/bin/env python3
import time
import webbrowser
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def open_website():
    raw_data = 'https://docs.google.com/spreadsheets/d/1_9KQgKxBTq6q1LAvkyFCjG7MrqccNB4-WRT45S6j2Bs/edit#gid=1088211518'
    webbrowser.open(raw_data)
    bet_link = 'https://azsao.me/'
    webbrowser.open(bet_link)
    time.sleep(5)
    pyautogui.press('esc')
    # pyautogui.click(1242, 804)
    # pyautogui.click(669, 470)

def open_bet_website():
    driver = webdriver.Chrome()
    bet_link = 'https://azsao.me/'
    driver.get(bet_link)
    driver.maximize_window()

def set_timer():
    return

try:
    open_website()
except KeyboardInterrupt:
    print("Done")