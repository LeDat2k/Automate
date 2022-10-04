#!/usr/bin/env python3  
from time import sleep
import pyautogui

def nohub(): 
    pyautogui.hotkey('alt', 'f2')
    sleep(0.5)

    # pyautogui.write('nohup ~/.local/bin/automate.py &')
    # pyautogui.write('nohup /media/dat/DISK/Dev/Automation/automate.py &')
    pyautogui.write('python3 /media/dat/DISK/Dev/Automation/automate.py')
    sleep(0.5)
    pyautogui.press('enter')

try:
    nohub()
except KeyboardInterrupt:
    print("Wrong")