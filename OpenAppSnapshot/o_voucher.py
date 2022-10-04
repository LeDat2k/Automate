#!/usr/bin/env python3
import webbrowser, pyautogui, time, subprocess

voucher_link = "https://magiamgiashopee.vn/"
buy_list = "https://docs.google.com/spreadsheets/d/1sffUT4YYb1LhjvG6nuV8XSxpKO2CVcmQmDTwTWDxFiI/edit#gid=0" 
clock = "https://time.is/"
notebook = "https://dynalist.io/d/s-9UMgdzlVr7FEf7BBRyQz_s"

def open_link():
	webbrowser.open(notebook)
	webbrowser.open(clock)
	# webbrowser.open(buy_list)
	time.sleep(0.1)
	webbrowser.open(voucher_link)
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'f')
	pyautogui.write('tu 0d'	)


if __name__ == '__main__':
	open_link()