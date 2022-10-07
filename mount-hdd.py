#!/usr/bin/env python3
import subprocess
import pyautogui
import time

def mount_hdd():
  command = 'sh -c "nemo"'
  subprocess.Popen(command.split())
  time.sleep(1)
  # pyautogui.hotkey('alt', 'f2')
  # time.sleep(0.1)
  # pyautogui.typewrite('nemo')
  # pyautogui.press('enter')
  # time.sleep(1)

  pyautogui.click(x=96, y=452)
  time.sleep(1)
  pyautogui.hotkey('alt', 'f4')

if __name__=="__main__":
  mount_hdd()
  