try:
	import pyautogui
	import time
	import os

	drive_url = "https://drive.google.com/drive/my-drive"
	pyautogui.hotkey('win', 'r')
	pyautogui.write(drive_url)
	pyautogui.press('enter')
	time.sleep(5)

	pyautogui.hotkey('shift', 'u')
	time.sleep(1)

	# get current pwd from terminal in python
	file_path = os.getcwd()
	???# get file name after command   
	file_name = ""
	pyautogui.hotkey('ctrl', 'l')
	pyautogui.write(file_path)
	pyautogui.press('tab')
	pyautogui.write(file_name)
	pyautogui.press('tab', presses=3)
	pyautogui.press('enter')
except Exception as bug:
	print(bug)

input()