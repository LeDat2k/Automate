#!/usr/bin/env python3

from genericpath import isdir
import os
from time import sleep
from pyautogui import press, hotkey

# folder=r'/media/dat/DISK/Notion/Class'
# for name in os.listdir(folder):
#     if name.endswith('.md'):
#         name_arr = name.split(' ')
#         del name_arr[-2]
#         print(name_arr)


press('f2')
press('right')
hotkey('ctrl', 'backspace')
press('backspace')
press('enter')
press('right')
