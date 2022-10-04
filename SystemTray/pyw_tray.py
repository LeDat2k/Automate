from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
import threading
import time
import sys
from icecream import ic

def create_image():
    return Image.open('python.ico')

def quit_tray(icon, item):
    icon.stop()
    e.set()

def system_tray():
    ic(menu(item('quit', quit_tray)))
    # ic(icon.stop())
    icon('pomodoro', create_image(), "Pomodoro Timer!", menu=menu(
        item('Quit', 
            quit_tray
        )
    )).run()

def count_down():
    e.wait(timeout=1)
    print('Done')
    e.wait(timeout=30)


# def main():
th1 = threading.Thread(target=system_tray)
th1.start()

e = threading.Event()    

count_down()

    
