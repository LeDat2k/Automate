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
    file_path = r'/media/dat/DISK/Note/Invest/News.md'

    now = str(date.today())

    with open(file_path, "a") as file:
        file.write('\n' + now + '\n')
        file.write('- ')

    os.system(f"subl {file_path}")

    # time.sleep(0.5)
    # pyautogui.hotkey('win', 'right')


# schedule.every().day.at("18:30").do(open_news)

# while True:
    # schedule.run_pending()
    # time.sleep(1)

# open_news()
