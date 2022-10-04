#!/usr/bin/env python3
import sys
import time
import subprocess
import os
import pyautogui
import webbrowser
from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('https://app.diagrams.net/')
# browser.quit()

def co_so_du_lieu():
  # cd to SQL folder
  SQL_PATH = '/media/dat/DISK/Dev/General/SQL'
  # pyautogui.press('f1') 
  # time.sleep(0.2)
  pyautogui.write('cd ' + SQL_PATH)
  pyautogui.press('enter')

  # code 
  subprocess.call(['code', SQL_PATH])

  # DBeaver
  pyautogui.press('win')
  time.sleep(0.2)
  pyautogui.write('DBeaver')
  time.sleep(0.2)
  pyautogui.press('enter')

  # open notion.so/course
  webbrowser.open('https://www.notion.so/lee2kzz/f75b5b82d80d4a6fb4162fdd20329f4c?v=499d782ff8d244d5bf0a81fccadbd138')
  return

def he_thong_thong_tin():
  # # cd /media/dat/DISK/Dev/Design/HeThongThongTin
  pyautogui.write('cd /media/dat/DISK/Dev/Design/HeThongThongTin')
  pyautogui.press('enter')

  # # open msteam
  webbrowser.open('https://teams.microsoft.com/_#/school/conversations/General?threadId=19:ZdkoYNWBvh7ZF4cgD4dHvuCObaXV7UQxJBMEGJ3FU901@thread.tacv2&ctx=channel')

  # open diagrams.net
  webbrowser.open('https://app.diagrams.net/')
  time.sleep(3.5)
  pyautogui.click(950, 520)
  return 

try:
  choice = input('''Open workspace for:
  1. Co so du lieu
  2. He thong thong tin
  ''')
  if choice == '1':
    co_so_du_lieu()
  elif choice == '2':
    he_thong_thong_tin()
  else:
    print('Quit!')
  
except KeyboardInterrupt:
  print('wrong')