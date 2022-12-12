#!/usr/bin/env python3

import datetime, time
import subprocess
from astral import LocationInfo
from astral.sun import sun
from icecream import ic

def timeline():
	city = LocationInfo('Hanoi', 'Viet Nam', 'Asia/Saigon', '21.083', '105.917')	
	c_data = sun(city.observer)
	
	sunrise = str(c_data['sunrise'])[11:16].split(':')
	sunset = str(c_data['sunset'])[11:16].split(':')

	sunrise = list(map(int, sunrise))
	sunset = list(map(int, sunset))

	# display +00:00 timezone => need add more 7 hours to +07:00 time zone
	sunrise[0] += 7 - 24
	sunset[0] += 7
	# Hanoi's dusk time later than Hue
	sunset[1] = abs(sunset[1] - 25)

	# assign time sunset vs sunrise
	now = datetime.datetime.now()
	sunrise = datetime.datetime(now.year, now.month, now.day, sunrise[0], sunrise[1])
	sunset = datetime.datetime(now.year, now.month, now.day, sunset[0], sunset[1])

	return sunrise, sunset

def light():
    light_command = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 1 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 1 -Type Dword -Force'
    process = subprocess.Popen(['powershell.exe', light_command])
    process.communicate()
    
def dark():
    dark_command = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 0 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force'
    process = subprocess.Popen(['powershell.exe', dark_command])
    process.communicate()
