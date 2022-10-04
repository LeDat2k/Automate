#!/usr/bin/env python3
import subprocess
import webbrowser

web_url = [
    "https://www.youtube.com/watch?v=4sQL7R5ySUU",
    "https://leetcode.com/problems/",
    "https://www.notion.so/lee1kzz/f75b5b82d80d4a6fb4162fdd20329f4c?v=499d782ff8d244d5bf0a81fccadbd138"
]
for i in web_url:
    webbrowser.open(i)

command = "code ~/Documents/test.py"
p = subprocess.Popen(command.split())

