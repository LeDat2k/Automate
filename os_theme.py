#!/usr/bin/env python3

import time
import webbrowser
from icecream import ic
import datetime

def save_time():
    with open('./stormgain_timestamp.md', 'w') as file:
        t_now = time.time()
        file.write(str(t_now))

def check_time():
    with open('./stormgain_timestamp.md', 'r') as file:
        t_stamp = file.read()
        # while time.time() - float(t_stamp) < 4*3600 + 30:
        #     time.sleep(1)
        # open_storm gain
        # save_time()
        
def open_stormgain():
    webbrowser.open('https://app.stormgain.com/crypto-miner/')

try:
    save_time()
    check_time()
except Exception as e:
    print(e.__class__)
    print(str(e))

