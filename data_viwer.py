'''
⠄⠄⠈⣿⠄⠄⠄⢙⢞⢿⣿⢹⢿⣦⢏⣱⢿⠘⣿⣝⠹⢿⣿⡽⣿⣿⣏⣆⢿⣿⡞⠁
⠄⠄⠄⢻⡀⠄⠄⠈⣾⡸⡏⢸⡾⣴⣿⣿⣶⣼⣎⢵⢀⡛⣿⣷⡙⡻⢻⡴⠨⠨⠖⠃
⠄⠄⠄⠈⣧⢀⡴⠊⢹⠁⡇⠈⢣⣿⣿⣿⣿⣦⣿⣷⣜⡳⣝⢧⢃⢣⣼⢁⠘⠆⠄⠄
⠄⠄⠄⠄⢹⡇⠄⣠⠔⠚⣅⠄⢰⣶⣦⣭⣿⣿⣿⡿⠟⠿⣷⡧⠄⣘⣟⣸⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢷⠎⠄⠄⠄⣼⣦⠻⣿⣿⡟⠛⠻⢿⣿⣿⣿⡾⢱⣿⡏⠸⡏⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠸⡄⠄⡄⠄⣿⢧⢗⠌⠻⣇⠿⠿⣸⣿⣿⡟⡐⣿⠟⢰⣇⠇⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣠⡆⠄⠃⢠⠏⣤⢀⢢⡰⣭⣛⡉⠩⠭⡅⣾⢳⡴⡀⢸⣿⡆⠄⠄⠄⠄
⠄⠄⠄⢀⣶⡟⣽⠼⢀⡕⢀⠘⠸⢮⡳⡻⡍⡷⡆⠤⠤⠭⢸⢳⣷⢸⡟⣷⠄⠄⠄⠄
'''

import os
import sys
import time

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from ui.A import A_form
from ui_controller.button_event import btn_events
from utils.load_data import data_loader
from configs import dataDir

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.data_dict = data_loader(dataDir)
        self.classes = self.data_dict.get_class_names()
        self.event = btn_events(self)
        self.ui = A_form(self, self, self.event)
        self.ui.list_classes.addItems(self.classes)
        self.ui.lab_title.setText("pics:" + str(self.data_dict.get_pics_num()))

    def set_button_red(self):
        self.ui.btn_makeJson.setEnabled(False)
        self.ui.btn_makeJson.setStyleSheet('QPushButton {background-color: #E24242; color: #E6E6E6;}')

    def set_button_back(self):
        self.ui.btn_makeJson.setEnabled(True)
        self.ui.btn_makeJson.setStyleSheet('QPushButton {background-color: #424242; color: #E6E6E6;}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())