import time
import ctypes
from icecream import ic
import os
from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
import threading, signal

exit_event = threading.Event()

# system tray to know if program is running,
def create_image():
    return Image.open('python.ico')

# exit system tray 
def quit_tray(icon, item):
    icon.stop()

def system_tray():
    icon('pomodoro', create_image(), "Pomodoro Timer!", menu=menu(
        item('Quit', 
            quit_tray
        )
    )).run()
    # wake thread 2
    exit_event.set()
    return True

# notify message upper and beyond
def notify(mins):
	text = f"It's been {mins} min, Let's take a rest!"
	title = 'Dialog'
	style = 1
	is_exit = ctypes.windll.user32.MessageBoxW(0, text, title, style)
    # return 1: click OK, 2: Cancel
	if is_exit == 1: return False
	if is_exit == 2: return True

def count_down(mins):
    print('Start pomodoro!')
    exit_event.wait(mins*60)
    # exit_event.wait(3)
    os.system("echo End!")

def main():
    break_time = 5
    pomodoro_time = 30
    exit_flag = False
    while True:
        count_down(pomodoro_time)
        if exit_flag == True:
            return
        exit_flag = notify(pomodoro_time)
        if exit_flag == True:
            # kill thread 1: system tray
            return

try:
    th1 = threading.Thread(target=system_tray)
    th1.start()

    th2 = threading.Thread(target=main)
    th2.start()

    th1.join()
    th2.join()

except KeyboardInterrupt:
    print("Wrong!")