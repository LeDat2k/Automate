#!/usr/bin/env python3
import time, datetime
from icecream import ic
import webbrowser

def main():
    ans = 5
    while ans>0:
        print("Running ...")
        now = datetime.datetime.now()
        webbrowser.open('https://app.stormgain.com/crypto-miner/')
        ans = ans-1
        # time.sleep(4*3600)

        if (now.hour+4)>23:
            next_time = datetime.datetime(now.year, now.month, now.day+1, now.hour+4-24, now.minute, now.second)
        else:
            next_time = datetime.datetime(now.year, now.month, now.day, now.hour+4, now.minute, now.second)

        while True:
            now_time = datetime.datetime.now()
            # ic(now_time)
            if now_time >= next_time:
                break
            time.sleep(1)

try:
    main()
except KeyboardInterrupt:
    print("Wrong")

    