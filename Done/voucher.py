import webbrowser, pyautogui, time, subprocess

def magiamgiashopee(toBuy, maGiamGia, clock):
	webbrowser.open(clock)
	webbrowser.open(toBuy)
	time.sleep(0.1)
	webbrowser.open(maGiamGia)
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'f')
	pyautogui.write('tu 0d')


def setAlarm():
	# open alarm
	command1 = "explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"
	p = subprocess.Popen(command1)
	p.communicate()

	# add new alarm
	pyautogui.hotkey('alt', '1')
	pyautogui.press('enter')
	pyautogui.press('tab', presses=4)
	pyautogui.press('enter')
	pyautogui.press('tab', presses=3)

	# set alarm's name = 'SHOPEE'
	pyautogui.write('SHOPEE')
	pyautogui.press('enter')

 
if __name__ == '__main__':
	maGiamGia = "https://magiamgiashopee.vn/"
	toBuy = "https://docs.google.com/spreadsheets/d/1sffUT4YYb1LhjvG6nuV8XSxpKO2CVcmQmDTwTWDxFiI/edit#gid=0" 
	clock = "https://time.is/"

	magiamgiashopee(toBuy, maGiamGia, clock)
	# setAlarm()
# test datetime in ls-l	
