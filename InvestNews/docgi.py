#!/usr/bin/env python3
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime
from icecream import ic

def vietstock(keyword):
  options = Options()
  options.headless = True
  driver = webdriver.Chrome(options=options)

  # driver = webdriver.Chrome()
  link = 'https://vietstock.vn/'
  driver.get(link)

  # turn off popup advertisement
  wait = WebDriverWait(driver, 10)
  wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div/div/div/a"))
  ).click()

  # click search box
  search_box = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div[1]/div[3]/form/div/div/input")
  search_box.click()

  # enter string to search box
  wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="popup-search-txt"]'))
  ).send_keys(keyword)

  # click to tag "Tin tuc"
  tintuc = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/ul/li[6]/span")
  tintuc.click()

  # click to the first result
  time.sleep(2)
  search = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[4]/div/div[5]/div[2]/div/div/ul/li[1]/a/div[2]/div")
  search.click()

  # Export to mardown file
  export_text(driver)

  driver.quit()

def vietstock():
  driver = webdriver.Chrome()
  link = 'https://vietstock.vn/chung-khoan/co-phieu.htm'
  driver.get(link)

  # click the first link (be careful cuz the first link only true if you click on time < 8:00 AM)
  driver.find_element(By.XPATH, '//*[@id="channel-container"]/section[1]/div/div/div[2]/h2').click()

  # Export to mardown file
  export_text(driver)

  driver.quit()  

def export_text(driver):
  now = datetime.now()
  date_now = now.strftime("%d-%m-%Y")
  file_path = '/media/dat/DISK/Dev/Automation/InvestNews/news/' + date_now + '.md'

  # body text
  content = driver.find_elements(By.ID, "vst_detail")

  # create and write file
  with open(file_path, 'w') as file:
    file.write(driver.current_url + '\n')
    for p in content:
      text = p.text.replace(' >>>', '\n>>>')
      file.write(text + '\n')

  # read file
  lines = []
  with open(file_path, 'r') as file:
    lines = file.readlines()

  # write file (remember for loop start at 0)
  with open(file_path, 'w') as file:
    for line_number, line_text in enumerate(lines):
      # remove line 2, line n, line n-1 (remember for loop start at 0)
      if line_number not in [1, len(lines)-1, len(lines)-2]:
        file.write(line_text)

def check_time():
  now = datetime.now()
  limit = datetime(now.year, now.month, now.day, 8, 0, 0)
  if now >= limit: 
    print(f"It's more than {limit}")
    vietstock("Doc gi truoc gio giao dich")
    return
  vietstock()
  
if __name__ == '__main__':
  check_time()

# schedule.every().monday.tuesday.wednesday.thursday.friday.at("06:01").do(vietstock, keyword="Doc gi truoc gio giao dich")
# schedule.every().monday.tuesday.wednesday.thursday.friday.at("08:01").do(vietstock, keyword="Top")