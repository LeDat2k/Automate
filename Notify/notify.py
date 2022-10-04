#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1919, 0, 400, 150)
        self.setWindowTitle("This is a notification")
        self.initUI()

    def initUI(self):
         # text - label view
        self.label = QtWidgets.QLabel(self)
        self.label.setText("This is a label!")
        self.label.move(50, 50)

        # button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("OK")
        self.b1.move(100, 100)
        # self.b1.clicked.connect(self.clicked)
        self.b1.clicked.connect(self.stormgain)
    
    def clicked(self):
        self.label.setText("You pressed")
        self.update()
    
    def update(self):
        self.label.adjustSize()
    
    def stormgain(self):
        webbrowser.open('https://app.stormgain.com/crypto-miner/')

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__': 
   window()

   