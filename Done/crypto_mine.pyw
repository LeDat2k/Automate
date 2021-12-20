#!/usr/bin/env python3
import time, datetime
from icecream import ic
import webbrowser

def main():
    print("Running ...")
    now = datetime.datetime.now()
    webbrowser.open('https://app.stormgain.com/crypto-miner/')
    time.sleep(4*3600-10)

try:
    main()
except KeyboardInterrupt:
    print("Wrong")

    