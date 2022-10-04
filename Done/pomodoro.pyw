import time
import ctypes
from icecream import ic
import os

# notify message upper and beyond
def notify(pomo, break_time):
	text = f"It's been {pomo} min, Let's CHECK YOUR PHONE then do some Stretch."
	title = 'Dialog'
	style = 1
	is_exit = ctypes.windll.user32.MessageBoxW(0, text, title, style)
    # return 1: click OK, 2: Cancel
	if is_exit == 1: return False
	if is_exit == 2: return True

def count_down(mins):
    print('Start pomodoro!')
    time.sleep(mins*60)
    # time.sleep(mins -26)
    os.system("echo End!")

def main():
    break_time = 5
    pomodoro_time = 30
    while True:
        count_down(pomodoro_time)
        if notify(pomodoro_time, break_time):
            return

try:
    main()
except KeyboardInterrupt:
    print("Wrong!")