#!/usr/bin/env python3
import webbrowser, pyautogui, datetime, time
import gspread
from icecream import ic
from datetime import date

def open_toilet_note():
    today = datetime.datetime.now().strftime('%d/%m/%Y')
    wks = gspread.service_account().open("PersonalData").worksheet("Toilet")

    # find last rows and the 1st column
    max_row = len(wks.get_all_values())
    # wks.update_cell(max_row + 1, 1, today)
    # ic(max_row)
    day_before = wks.cell(max_row, 1).value.split('/')
    print(date.today())


    # ic(today)
    # if (wks.cell(max_row, 1).value == today):
    #     print("1")

    
open_toilet_note()

