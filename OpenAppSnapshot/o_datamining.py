#!/usr/bin/env python3  

import subprocess
import pyautogui

# ?? how to save current opening file path 

with open('datamining.txt', 'r') as file:
    paths = file.readlines()
    for path in paths:
        command = "xdg-open " + path
        subprocess.Popen(command.split())
# save path of file to text file called: recent.txt
# read recent.txt
# run commmand xdg-open for each file_path in recent.txt
