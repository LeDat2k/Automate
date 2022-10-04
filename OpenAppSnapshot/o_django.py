#!/usr/bin/env python3
import subprocess
import webbrowser
import time

try:
    # open document
    DJANGO_LINK = 'https://docs.djangoproject.com/en/4.0/'
    webbrowser.open(DJANGO_LINK)


    # open terminal and move to DjangoLearning

    # open code in DjangoLearning 
    command = 'code /media/dat/DISK/Dev/Web/DjangoLearning'
    subprocess.Popen(command.split())

except KeyboardInterrupt:
    print("Wrong")