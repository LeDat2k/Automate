#!/usr/bin/env python3
import time, pyautogui
from icecream import ic
import webbrowser
from datetime import datetime

def click_button():
    pyautogui.click(x=958, y=575)

def main():
    while True:
        print("Running ...")
        now = datetime.now()

        if (now.hour+4)>23:
            next_time = datetime(now.year, now.month, now.day+1, now.hour+4-24, now.minute, now.second)
        else:
            next_time = datetime(now.year, now.month, now.day, now.hour+4, now.minute, now.second)

        while True:
            now_time = datetime.now()
            # ic(now_time)
            if now_time >= next_time:
                webbrowser.open('https://app.stormgain.com/crypto-miner/')
                break
            time.sleep(1)

try:
    main()
except KeyboardInterrupt:
    print("Wrong")

    