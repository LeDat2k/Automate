#!/usr/bin/env python3
import subprocess
import time
import webbrowser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import schedule

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

def print_now():
  print(time.ctime())

def print_GFG():
  print("GFG")
  
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
 
# Adding an icon
icon_absolute_path = '/media/dat/DISK/Dev/Automation/SystemTray/icon.png'
# icon_path = 'icon.png'
icon = QIcon(icon_absolute_path)
  
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
tray.setToolTip("Check my tray")
  
# # Creating the options
menu = QMenu()
# option1 = QAction("Geeks for Geeks")
# option1.triggered.connect(print_now)
# menu.addAction(option1)

# option2 = QAction("GFG")
# option2.triggered.connect(print_GFG)
# menu.addAction(option2)

# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)

sys.exit(app.exec_())


# try:
#   while True:
#     schedule.run_pending()
#     time.sleep(1)

# except KeyboardInterrupt:
#   print("\tTerminate!")
