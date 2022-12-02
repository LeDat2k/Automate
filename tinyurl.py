#!/usr/bin/env python3
# !pip install pyshorteners, pyperclip
import pyshorteners 
import pyperclip 
from sys import argv
import os

try:
    # link_input  = input('What link would you like to shorten?\n')
    link_input  = argv[1] 
    shortener = pyshorteners.Shortener()
    url = shortener.tinyurl.short(link_input)
    pyperclip.copy(url) 
except Exception as e:
    print(e.__class__)
    print(str(e))
    os.system(f'notify-send "Tiny url: {e.__class__}" "{str(e)}"')