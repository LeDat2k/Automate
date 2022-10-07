#!/usr/bin/env python3  
from time import sleep
import pyautogui
import os
import subprocess

def nohub(): 
    # pyautogui.hotkey('alt', 'f2')
    # sleep(0.5)

    # pyautogui.write('nohup ~/.local/bin/automate.py &')
    # pyautogui.write('nohup /media/dat/DISK/Dev/Automation/automate.py &')
    # pyautogui.write('python3 /media/dat/DISK/Dev/Automation/automate.py')
    # sleep(0.5)
    # pyautogui.press('enter')

    # os.system("/media/dat/DISK/Dev/Automation/automate.py")
    
    subprocess.Popen("/media/dat/DISK/Dev/Automation/automate.py")

try:
    nohub()
except KeyboardInterrupt:
    print("Wrong")