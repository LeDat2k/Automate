#!/usr/bin/env python3

import time
import webbrowser
from icecream import ic
import datetime
import os, random

# def save_time():
#     with open('./stormgain_timestamp.md', 'w') as file:
#         t_now = time.time()
#         file.write(str(t_now))

# def check_time():
#     with open('./stormgain_timestamp.md', 'r') as file:
#         t_stamp = file.read()
#         # while time.time() - float(t_stamp) < 4*3600 + 30:
#         #     time.sleep(1)
#         # open_storm gain
#         # save_time()
        

def check_time(light_time: str, dark_time: str):
    light = light_time.split(':')
    dark = dark_time.split(':')

    light = datetime.time(int(light[0]), int(light[1]))
    dark = datetime.time(int(dark[0]), int(dark[1]))

    if datetime.datetime.now().time() >= dark:
        change('dark')
    else:
        change('light')


# sunrise(Mint-Y) vs sunset(Mint-Y-Dark):
def change(mode):
    if mode == 'light':
        mode = ''
    else:
        mode = 'Dark-'

    colors = ["Aqua", "Blue", "Brown", "Grey", "Orange", "Pink", "Purple", "Red", "Sand", "Teal"]
    name = "Mint-Y-" + mode + random.choice(colors)
    # Mint-Y-Aqua
    commands = [
        f'gsettings set org.cinnamon.desktop.interface gtk-theme {name}',
        f'gsettings set org.cinnamon.theme name {name}'
    ]
    for command in commands:
        os.system(command)


try:
    # save_time()
    # check_time()
    # change()
    
    pass
except Exception as e:
    print(e.__class__)
    print(str(e))

