import pyautogui
import time
from icecream import ic

def auto_roll(seconds):
    time.sleep(seconds)
    pyautogui.press('PgDn')

# check if chrome, 
# check if metruyen.com tab
# reset timer if press Page Down

# import psutil

# def if_process_is_running_by_exename(exename='chrome.exe'):
#     for proc in psutil.process_iter(['pid', 'name']):
#         # This will check if there exists any process running with executable name
#         if proc.info['name'] == exename:
#             return True
#     return False

try:
    seconds = 30
    print('Running...') 
    # while True:
    #     auto_roll(senconds)
    # if_process_is_running_by_exename()
    
except KeyboardInterrupt:
    print('Wrong')