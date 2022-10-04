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

from test import print_now 

class MySystemTray(QSystemTrayIcon):
    def __init__(self):
        super(MySystemTray, self).__init__()
        self.init_tray()
    
    def quit_tray(self):
        # self.close()
        print("Quit")

    def init_tray(self):
        icon_absolute_path = '/media/dat/DISK/Dev/Automation/SystemTray/icon.png'
        icon = QIcon(icon_absolute_path)

        self.setIcon(icon)
        self.setVisible(True)
        self.setToolTip("Automate!")

        # Adding item on the menu bar
        # Creating the options
        menu = QMenu()
        # To quit the app
        quit = QAction("Quit")
        quit.triggered.connect(self.quit_tray)
        menu.addAction(quit)

        # Adding options to the System Tray
        self.setContextMenu(menu)

        print("song")
        

def system_tray():
    app = QApplication(sys.argv)
    tray = MySystemTray()
    tray.show()
    sys.exit(app.exec_())

try:
    system_tray()
except KeyboardInterrupt:
    print("Wrong")    

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.setGeometry(1919, 0, 400, 150)
#         self.setWindowTitle("Notification")
#         self.initUI()

#     def initUI(self):
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("Time to mine!")

#         # button
#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("OK")
#         self.b1.move(100, 100)
#         self.b1.clicked.connect(self.stormgain)
    
#     def stormgain(self):
#         webbrowser.open('https://app.stormgain.com/crypto-miner/')
#         self.close()

# def window_stormgain():
#     app = QApplication(sys.argv)
#     win = MyWindow()

#     win.show()
#     app.exec_()

# ------------------------------------------
# webbrowser.open('https://app.stormgain.com/crypto-miner/')
# schedule.every(4*3600 + 30).seconds.do(window_stormgain)
  
# app = QApplication(sys.argv)
# app.setQuitOnLastWindowClosed(False)
 
# # Adding an icon
# icon_absolute_path = '/media/dat/DISK/Dev/Automation/icon.png'
# icon_relative_path = 'icon.png'
# icon = QIcon(icon_absolute_path)

# # Adding item on the menu bar
# tray = QSystemTrayIcon()
# tray.setIcon(icon)
# tray.setVisible(True)
# tray.setToolTip("Automate!")
  
# # Creating the options
# menu = QMenu()
# # To quit the app
# quit = QAction("Quit")
# quit.triggered.connect(app.quit)
# menu.addAction(quit)

# # Adding options to the System Tray
# tray.setContextMenu(menu)

# sys.exit(app.exec_())

# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\tTerminate!")
