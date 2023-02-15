#!/usr/bin/env python3

import subprocess
from astral import LocationInfo
from astral.sun import sun
from icecream import ic
import datetime
import os
import random
from sys import platform


def change_by_time(light_time: datetime.time, dark_time: datetime.time):
    now = datetime.datetime.now().time()
    if now >= dark_time or now <= light_time:
        change('dark')
    else:
        change('light')


def change(mode):
    if platform == "linux" or platform == "linux2":
        type = '' if mode == 'light' else 'Dark-'

        colors = ["Aqua", "Blue", "Brown", "Grey", "Orange",
                  "Pink", "Purple", "Red", "Sand", "Teal"]
        name = "Mint-Y-" + type + random.choice(colors)

        # sunrise(Mint-Y) vs sunset(Mint-Y-Dark):
        # Mint-Y-Aqua
        commands = [
            f'gsettings set org.cinnamon.desktop.interface gtk-theme {name}',
            f'gsettings set org.cinnamon.theme name {name}'
        ]

        for command in commands:
            os.system(command)

    elif platform == "darwin":
        print("I haven't use Mac")

    elif platform == "win32":
        light_command = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 1 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 1 -Type Dword -Force'
        dark_command = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 0 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force'

        command = light_command if mode == 'light' else dark_command

        subprocess.Popen(['powershell.exe', command])


try:
    # save_time()
    # check_time()
    # change('dark')

    pass
except Exception as e:
    print(e.__class__)
    print(str(e))
