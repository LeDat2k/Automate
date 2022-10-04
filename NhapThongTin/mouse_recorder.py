#!/usr/bin/env python3
import pyautogui
from pynput.keyboard import Key, Listener
import pyperclip

mouse_locations = []
# when you release 'ctrl' mouse's location
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    
    if key == Key.ctrl:
        print("Mouse's location saved!!")
        x, y = pyautogui.position()
        mouse_locations.append((x, y))
        pyperclip.copy(str(mouse_locations))

try:
    # Collect events until released
    with Listener(
            # on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

except KeyboardInterrupt:
    print(mouse_locations)

