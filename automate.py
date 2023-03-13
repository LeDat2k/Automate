#!/usr/bin/env python3
import datetime
import os
import subprocess
import time
import webbrowser
from multiprocessing import Process

import gspread
import pyautogui
import requests
import schedule

import news
import os_theme

# sys.path.append("/media/dat/DISK/Dev/Automation/Shopee")
# import shopee
# from Shopee import shopee


def wait_internet():
    url = "https://www.google.com"
    timeout = 5
    while True:
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            time.sleep(1)


def next_tab():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


def claim_shopee_coin():
    wait_internet()

    # shopee.claim_coin()
    webbrowser.open("https://shopee.vn/shopee-coins/")


def check_mail():
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')


def open_invest():
    urls = [
        # 'https://fireant.vn/dashboard',
        'https://vietstock.vn/chung-khoan/co-phieu.htm',
        'https://www.tradingview.com/symbols/HOSE-VNINDEX/'
    ]
    for url in urls:
        webbrowser.open(url)


def track_habit():
    wait_internet()
    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1_9KQgKxBTq6q1LAvkyFCjG7MrqccNB4-WRT45S6j2Bs/edit#gid=859944615')


def report_budget():
    wait_internet()
    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1zA7TlchlQHoFkFKrLQgHuXRAR-Rwfq0He0ASi-N_S2M/edit#gid=1732160294')

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    worksheet = gspread.service_account().open("MonthlyBudget").worksheet("Transactions")

    # Find the length of the worksheet from column A to D
    max_row = 0
    for i in range(1, 5):
        if worksheet.col_count >= i:
            if worksheet.col_values(i):
                if len(worksheet.col_values(i)) > max_row:
                    max_row = len(worksheet.col_values(i))

    worksheet.update_cell(max_row + 1, 1, today)
    worksheet.update_cell(max_row + 1, 4, "Everyday-Food")


def review_vocabulary():
    commmand = 'anki'
    subprocess.Popen(commmand.split())


def claim_stormgain():
    wait_internet()
    webbrowser.open('https://app.stormgain.com/crypto-miner/')


def grateful():
    commands = [
        'subl /media/dat/DISK/Note/Personality/Mistake.md',
        'subl /media/dat/DISK/Note/Personality/Grateful.md'
    ]

    for command in commands:
        os.system(command)


schedule.every().day.at("05:00").do(grateful)
schedule.every().day.at("05:00").do(claim_shopee_coin)
schedule.every().day.at("05:00").do(open_invest)
schedule.every().day.at("05:00").do(claim_stormgain)
schedule.every().day.at("05:00").do(review_vocabulary)
schedule.every().day.at("12:30").do(check_mail)
schedule.every().day.at("18:30").do(news.update)
schedule.every().day.at("21:00").do(track_habit)
schedule.every().day.at("21:00").do(report_budget)

# ---------------------------------------------------
light_time = datetime.time(7, 50)
dark_time = datetime.time(17, 00)

# schedule.every().day.at(light_time.strftime("%H:%M")
#                         ).do(os_theme.change, mode='light')
# schedule.every().day.at(dark_time.strftime("%H:%M")
#                         ).do(os_theme.change, mode='dark')

# -----------------------------------------------------
claim_shopee_coin()
# os_theme.change_by_time(light_time, dark_time)

while True:
    schedule.run_pending()
    time.sleep(1)

# review_vocabulary()
