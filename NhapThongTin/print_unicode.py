#!/usr/bin/env python3  
import pyautogui 
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyautogui
import pyperclip
import platform

pyautogui.click(x=828, y=694)

def type(text):    
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")


# type("It's leviOsa, not lêvioçÁ!")
df = pd.read_csv('Thongtin.csv', sep=',') 
name = str(df.iloc[1, 0])
# name = "lê phước đạt"
# type(name)

type(name)

