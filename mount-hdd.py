#!/usr/bin/env python3
import subprocess
import pyautogui
import time

def mount_hdd_file_explorer():
  # open file explorer
  command = 'sh -c "nemo"'
  subprocess.Popen(command.split())
  time.sleep(2)

  # Click as DISK position
  pyautogui.click(x=96, y=515)
  time.sleep(1)
  pyautogui.hotkey('alt', 'f4')

def mount_hdd_by_disks():
  command = 'sh -c "gnome-disks"'
  subprocess.Popen(command.split())
  time.sleep(0.5)
  pyautogui.click(1920/2, 1080/2)
  time.sleep(0.5)
  pyautogui.click(749, 589)
  time.sleep(1.5)
  pyautogui.hotkey('alt', 'f4')


  
if __name__=="__main__":
  # mount_hdd_file_explorer()
  mount_hdd_by_disks()

  # TODO: the best way to mount DISK: linux - command
    


  