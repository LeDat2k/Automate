#!/usr/bin/env python3
import subprocess
import pyautogui, sys, os


#### ?? danger: Create .screenshot.png which I don't need
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = '(' + str(x).rjust(4) + ',' + str(y).rjust(4) + ')'
        print(positionStr, end='')

        img = pyautogui.screenshot()
        pixelColor = img.getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'

        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
except KeyboardInterrupt:
    # print('\n')
    print("Wrong")
    command = 'rm /media/dat/DISK/Dev/Automation/NhapThongTin/.*.png'
    subprocess.Popen(command.split())


# img = pyautogui.screenshot()

# print(img.getpixel(pyautogui.position()))