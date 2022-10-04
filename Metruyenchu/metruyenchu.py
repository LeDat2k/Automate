#!/usr/bin/env python3
import asyncio
import os, time
from pathlib import Path
import sys
from pynput.keyboard import Key, Listener
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service

# print all choice in text file
def read_list(path):
    with open(path,"r") as file:
        result = [] 
        for i in file.readlines():
            result.append(i.replace('\n', ''))
    return result

def show_list(choices):
    dict = {}
    for i, choice in enumerate(choices):
        print(f"{i}. {choice}")
        dict[str(i)] = choice

    choice = (input("Enter your choice (Enter 'edit' for CRUD novel list): "))
    if choice.lower() == "edit":
        working_dir = Path(__file__).absolute().parent
        novels_path = os.path.join(working_dir, "truyen.md")
        os.system(f'subl {novels_path}')
        return

    if choice in dict.keys():
        open_web(dict[choice])
        return

    choice = input("Nhap ten truyen(chinh xac): ")
    open_web(choice)

def open_web(novel):
    site = 'https://metruyenchu.com/truyen/'
    search_url = site + novel.replace(' ', '-') 

    options = Options()
    options.add_argument("start-maximized")
    driver_service = Service(executable_path="/media/dat/DISK/Dev/Automation/BrowserDrivers/chromedriver")
    driver = webdriver.Chrome(service=driver_service, options=options)

    # driver_service = Service(executable_path="/media/dat/DISK/Dev/Automation/BrowserDrivers/geckodriver")
    # driver = webdriver.Firefox(service=driver_service, options=options)

    driver.get(search_url)
    time.sleep(30)
    driver.find_element(By.XPATH, '//*[@id="nav-tab-chap"]').click()

    wait = WebDriverWait(driver, 30)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="chapter-list"]/div/div[2]/div/div[1]/a/div'))
    )

    driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div/div[1]/button/i').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div/div[2]/div/div[1]/a/div/div').click()

    # dark theme
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="js-menu-actions"]/li[2]/a').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="js-themes-picker"]/li[7]/a').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="js-menu-actions"]/li[2]/div/button').click()
    
    with Listener(
            on_press=on_press,
            # on_release=on_release
        ) as listener:
        listener.join()


def on_press(key):
    if key == Key.esc:
        # Stop listener
        return False
    
if __name__=="__main__": 
    working_dir = Path(__file__).absolute().parent
    novels_path = os.path.join(working_dir, "truyen.md")

    try:
        show_list(read_list(novels_path))
    except KeyboardInterrupt:
        print("\nSomething wrong!")
    else:
        print("\nSuccessful!")
    finally:
        print("Done!")

    # create 
    # Update
    # Delete
    









