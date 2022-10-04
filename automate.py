#!/usr/bin/env python3
import datetime
import os
import webbrowser
import pyautogui
import requests
import schedule
import time
import random
import gspread
from multiprocessing import Process
import sys
# sys.path.append("/media/dat/DISK/Dev/Automation/Shopee")
# import shopee
from Shopee import shopee


def wait_internet():
    url = "https://www.google.com"
    timeout = 5
    while True:
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            time.sleep(1)


def check_change_theme(light_time: str, dark_time: str):
    light = light_time.split(':')
    dark = dark_time.split(':')

    light = datetime.time(int(light[0]), int(light[1]))
    dark = datetime.time(int(dark[0]), int(dark[1]))

    if datetime.datetime.now().time() >= dark:
        change_theme('dark')
    else:
        change_theme('light')


# sunrise(Mint-Y) vs sunset(Mint-Y-Dark):
def change_theme(theme_mode):
    if theme_mode == 'light':
        theme_mode = ''
    else:
        theme_mode = 'Dark-'

    theme_colors = ["Aqua", "Blue", "Brown", "Grey", "Orange", "Pink", "Purple", "Red", "Sand", "Teal"]
    theme_name = "Mint-Y-" + theme_mode + random.choice(theme_colors)
    # Mint-Y-Aqua
    commands = [
        f'gsettings set org.cinnamon.desktop.interface gtk-theme {theme_name}',
        f'gsettings set org.cinnamon.theme name {theme_name}'
    ]
    for command in commands:
        os.system(command)


def open_shopee_coin():
    wait_internet()

    shopee.claim_coin()


# scheduler1 = schedule.Scheduler()
# p1 = Process(target=open_shopee_coin)
# scheduler1.every().day.at("05:00").do(p1.start)
schedule.every().day.at("05:00").do(open_shopee_coin)


def open_gmail():
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


schedule.every().day.at("12:30").do(open_gmail)


def notify_remitano():
    os.system('notify-send "Remitano" "Open Remitano app on your phone!"')


schedule.every(24 * 60 + 10).minutes.do(notify_remitano)


def open_invest():
    urls = [
        # 'https://fireant.vn/dashboard',
        'https://vietstock.vn/chung-khoan/co-phieu.htm',
        # 'https://dynalist.io/d/dQshRzOg9BbUfzTAc0lnjh64',
        'https://www.tradingview.com/symbols/HOSE-VNINDEX/'
    ]
    for url in urls:
        webbrowser.open(url)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


schedule.every().day.at("05:00").do(open_invest)


def open_toilet_note():
    wait_internet()

    webbrowser.open(
        'https://docs.google.com/spreadsheets/d/1_9KQgKxBTq6q1LAvkyFCjG7MrqccNB4-WRT45S6j2Bs/edit#gid=859944615')

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')

    today = datetime.datetime.now().strftime('%d/%m/%Y')
    wks = gspread.service_account().open("PersonalData").worksheet("Toilet")

    # find last rows and the 1st column
    max_row = len(wks.get_all_values())
    wks.update_cell(max_row + 1, 1, today)


schedule.every().day.at("21:00").do(open_toilet_note)


def open_monthly_budget():
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


schedule.every().day.at("21:00").do(open_monthly_budget)


# class MyWindow(QMainWindow):
#   def __init__(self):
#     super(MyWindow, self).__init__()
#     self.setGeometry(1919, 0, 400, 150)
#     self.setWindowTitle("Notification")
#     self.initUI()

#   def initUI(self):
#     self.label = QtWidgets.QLabel(self)
#     self.label.setText("Time to mine!")

#     # button
#     self.b1 = QtWidgets.QPushButton(self)
#     self.b1.setText("OK")
#     self.b1.move(100, 100)
#     self.b1.clicked.connect(self.stormgain)

#   def stormgain(self):
#     webbrowser.open('https://app.stormgain.com/crypto-miner/')
#     self.close()

# def window_stormgain():
#   app = QApplication(sys.argv)
#   win = MyWindow()

#   win.show()
#   # sys.exit(app.exec_())
#   app.exec_()
# ------------------------------------------

def window_stormgain():
    wait_internet()
    # check_stormgain_time()
    webbrowser.open('https://app.stormgain.com/crypto-miner/')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')


schedule.every(4 * 60 + 30).minutes.do(window_stormgain)

# ---------------------------------------------------
light_time = "06:30"
dark_time = "18:00"
schedule.every().day.at(light_time).do(change_theme, theme_mode='light')
schedule.every().day.at(dark_time).do(change_theme, theme_mode='dark')

# -----------------------------------------------------
# Neu su dung thi se co them 1 process <defunct> python3 run in background
# Process(target=open_shopee_coin).start()
open_shopee_coin()
open_gmail()
open_invest()
# open_monthly_budget()
# open_toilet_note()
check_change_theme(light_time, dark_time)

while True:
    # scheduler1.run_pending()
    schedule.run_pending()
    time.sleep(1)
