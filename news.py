#!/usr/bin/env python3

import os
import webbrowser
import schedule
import time
from datetime import date
import pyautogui


def open_news():
    webbrowser.open("https://www.youtube.com/c/vtv24/videos")

    # write date
    os.system("subl /media/dat/DISK/Note/Invest/News.md")
    now = str(date.today())

    with open("/media/dat/DISK/Note/Invest/News.md", "a") as file:
        file.write(now + '\n')
        file.write('- ')


schedule.every().day.at("18:30").do(open_news)

while True:
    schedule.run_pending()
    time.sleep(1)
