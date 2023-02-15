#!/usr/bin/env python3
import subprocess
import pyautogui
import time

def mount_hdd():
  # open file explorer
  command = 'sh -c "nemo"'
  subprocess.Popen(command.split())
  time.sleep(2)

  # Click as DISK position
  pyautogui.click(x=96, y=515)
  time.sleep(1)
  pyautogui.hotkey('alt', 'f4')

if __name__=="__main__":
  mount_hdd()
  