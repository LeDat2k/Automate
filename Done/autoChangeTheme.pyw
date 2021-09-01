#!/usr/bin/env python3

import datetime, time
import wintheme
from icecream import ic

def main():
    print("Running...")

    light_time, dark_time = wintheme.timeline()
    # dark_time = datetime.datetime(2021,8,29,17,7,0)

    now = datetime.datetime.now()
    if now >= light_time and now < dark_time:
        is_light = True
        n_change = 1 # 1 times to change theme then end the program
        wintheme.light()
    else:
        is_light = False
        wintheme.dark()
        if now>light_time:
            n_change = 2 # 2 times to change theme then end the program
        else:
            n_change = 0

    while True:
        if n_change == 0:
            break

        now = datetime.datetime.now()
        if now >= light_time and now < dark_time:
            if not is_light:
                wintheme.light()
                is_light = True
                n_change -= 1
                # t_sleep = (dark_time-now).seconds
                # time.sleep(t_sleep)
        else:
            if is_light:
                wintheme.dark()
                is_light = False
                n_change -= 1

        time.sleep(60)
        # ic(is_light)
 
try:
    main()
except KeyboardInterrupt:
    print('Wrong')
