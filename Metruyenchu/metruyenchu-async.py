#!/usr/bin/env python3

import asyncio
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def read_list(path):
    with open(path,"r") as file:
        result = [] 
        for i in file.readlines():
            result.append(i.replace('\n', ''))
    return result

def metruyenchu(driver, novel):
    start_time = time.time()
    site = 'https://metruyenchu.com/truyen/'
    search_url = site+novel.replace(' ', '-') 
    driver.get(search_url)
    driver.find_element(By.XPATH, '//*[@id="nav-tab-chap"]').click()

    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="chapter-list"]/div/div[2]/div/div[1]/a/div'))
    )

    driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div/div[1]/button/i').click()
    time.sleep(1)
    # await asyncio.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div/div[2]/div/div[1]/a/div/div').click()

    driver.switch_to.new_window('tab')
    print(f"Done: {time.time()-start_time}")
    
# async def main():
if __name__=="__main__": 
    PATH = "./truyen.md"
    novels = read_list(PATH)

    options = Options()
    options.add_argument('--disable-notifications')
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")

    # options.headless = True
    driver_service = Service(executable_path="/media/dat/DISK/Dev/Automation/BrowserDrivers/chromedriver")
    driver = webdriver.Chrome(service=driver_service, options=options)

    for novel in novels:
        metruyenchu(driver, novel)
    
    # tasks = [metruyenchu(driver, novel) for novel in novels]
    # await asyncio.gather(*tasks)

# main()
# asyncio.run(main())

    