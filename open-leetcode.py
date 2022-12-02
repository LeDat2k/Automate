#!/usr/bin/env python3
import os
import webbrowser

webbrowser.open("https://neetcode.io/practice")
webbrowser.open("https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0")
# username = os.getlogin()
username = "dat" 
os.system(f"code /media/{username}/DISK/Dev/Python/Test")
os.system(f'subl /media/{username}/DISK/Note/Dev/Course/LeetCode.md')