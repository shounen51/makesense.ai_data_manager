import json
import time
import sys
from datetime import datetime
import random
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests

from configs import *
from utils.utils import *
from utils.output_data import make_json


class btn_events():
    def __init__(self, main_window):
        self.main = main_window
        self.out_json = make_json(self.main, self.main.classes)

    def class_click(self):
        className = self.main.ui.list_classes.currentItem().text()
        label = self.main.ui.lab_title
        pic_list = self.main.data_dict.get_classes_pics(className)
        self.main.ui.list_pics.clear()
        self.main.ui.list_pics.addItems(pic_list)
        label.setText(f"{className} pics: {len(pic_list)} / {self.main.data_dict.get_pics_num()} ({round(len(pic_list)/self.main.data_dict.get_pics_num()*100, 2)}%)")

    def pic_click(self):
        label = self.main.ui.lab_pic
        _list = self.main.ui.list_labels
        pic_name = self.main.ui.list_pics.currentItem().text()
        pic_dict = self.main.data_dict.get_pic_dict(pic_name)
        pic_path = pic_dict['filename']
        self.frame = darw_regions_and_label_list(pic_path, pic_dict, label, _list)
        

    def label_click(self):
        pass

    def make_json(self):
        self.out_json.setting(dataDir, 0.7)
        self.out_json.start()