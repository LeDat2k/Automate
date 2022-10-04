import pyautogui, time, webbrowser

def manipulate():
	webbrowser.open('https://gitexercises.fracz.com/committer/cxk')

	#open wsl terminal
	pyautogui.hotkey('win')
	pyautogui.write('wsl')
	pyautogui.press('enter')
	time.sleep(1)
	
	pyautogui.write('z exercises')
	pyautogui.press('enter')
	time.sleep(0.2)

	pyautogui.write('git start')
	pyautogui.press('enter')

	pyautogui.hotkey('win', 'right')	
	pyautogui.press('esc')

if __name__ == '__main__':
	manipulate()