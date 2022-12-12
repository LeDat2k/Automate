#!/usr/bin/env python3
import datetime
import os
import webbrowser
import pyautogui
import requests
import schedule
import time
import gspread
from multiprocessing import Process
import sys
import subprocess
# sys.path.append("/media/dat/DISK/Dev/Automation/Shopee")
# import shopee
# from Shopee import shopee
import news
import os_theme


def wait_internet():
    url = "https://www.google.com"
    timeout = 5
    while True:
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            time.sleep(1)


def claim_shopee_coin():
    wait_internet()

    # shopee.claim_coin()
    webbrowser.open("https://shopee.vn/shopee-coins/")


def check_mail():
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


def open_invest():
    urls = [
        # 'https://fireant.vn/dashboard',
        'https://vietstock.vn/chung-khoan/co-phieu.htm',
        'https://www.tradingview.com/symbols/HOSE-VNINDEX/'
    ]
    for url in urls:
        webbrowser.open(url)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


def track_habit():
    wait_internet()

    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1_9KQgKxBTq6q1LAvkyFCjG7MrqccNB4-WRT45S6j2Bs/edit#gid=859944615')

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


def report_budget():
    wait_internet()

    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1zA7TlchlQHoFkFKrLQgHuXRAR-Rwfq0He0ASi-N_S2M/edit#gid=1732160294')

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')

    today = datetime.datetime.now().strftime('%d/%m/%Y')
    wks = gspread.service_account().open("MonthlyBudget").worksheet("Transactions")

    # find last rows and the 1st column
    max_row = len(wks.get_all_values())
    wks.update_cell(max_row + 1, 1, today)
    wks.update_cell(max_row + 1, 4, "Everyday-Food")


def review_vocabulary():
    commmand = 'anki'
    subprocess.Popen(commmand.split())


def claim_stormgain():
    wait_internet()
    # check_stormgain_time()
    webbrowser.open('https://app.stormgain.com/crypto-miner/')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def grateful():
    commands = [
        'subl /media/dat/DISK/Note/Personal/Mistake.md',
        'subl /media/dat/DISK/Note/Personal/Grateful.md'
    ]

    for command in commands:
        os.system(command)


schedule.every().day.at("05:00").do(grateful)
schedule.every().day.at("05:00").do(claim_shopee_coin)
schedule.every().day.at("05:00").do(open_invest)
schedule.every().day.at("05:10").do(review_vocabulary)
schedule.every().day.at("12:30").do(check_mail)
schedule.every().day.at("18:30").do(news.update)
schedule.every().day.at("21:00").do(track_habit)
schedule.every().day.at("21:00").do(report_budget)
schedule.every(4 * 60 + 30).minutes.do(claim_stormgain)

# ---------------------------------------------------
light_time = "07:30"
dark_time = "17:00"
schedule.every().day.at(light_time).do(os_theme.change, mode='light')
schedule.every().day.at(dark_time).do(os_theme.change, mode='dark')

# -----------------------------------------------------
# claim_shopee_coin()
# check_mail()
# open_invest()
os_theme.change_by_time(light_time, dark_time)

while True:
    schedule.run_pending()
    time.sleep(1)
