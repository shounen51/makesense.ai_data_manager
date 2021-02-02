# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Joseph\git\Taipei_MOT_UI\test\A.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.color import *
from ui_controller.my_widgets import *

class A_form(QtWidgets.QWidget):
    def __init__(self, Form, main, event):
        QtWidgets.QWidget.__init__(self)
        # Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(1460, 920)
        Form.setMinimumSize(QtCore.QSize(1920, 1080))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        Form.setAutoFillBackground(True)
        Form.setPalette(back_plt)

        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)

        self.lab_title = my_label(Form)
        self.lab_title.setFont(font)
        self.lab_title.setGeometry(QtCore.QRect(270, 10, 1391, 91))
        self.lab_title.setObjectName("label")
        self.lab_title.setAlignment(QtCore.Qt.AlignCenter)
        self.list_classes = my_list(Form)
        self.list_classes.setGeometry(QtCore.QRect(10, 110, 251, 841))
        self.list_classes.setObjectName("listWidget")
        self.list_classes.setFont(font)
        self.list_pics = my_list(Form)
        self.list_pics.setGeometry(QtCore.QRect(270, 110, 251, 841))
        self.list_pics.setObjectName("listWidget")
        self.list_pics.setSortingEnabled(True)
        self.lab_pic = clickable_label(Form, event)
        self.lab_pic.setGeometry(QtCore.QRect(530, 110, 1121, 841))
        self.lab_pic.setObjectName("label_2")
        # self.lab_pic.setStyleSheet("background-image: url(./src/0000_mv.jpg);")
        self.list_labels = my_list(Form)
        self.list_labels.setFont(font)
        self.list_labels.setGeometry(QtCore.QRect(1660, 110, 251, 841))
        self.list_labels.setObjectName("listWidget")
        self.list_labels.setSortingEnabled(True)
        self.btn_makeJson = my_btn(Form)
        self.btn_makeJson.setFont(font)
        self.btn_makeJson.setGeometry(QtCore.QRect(1660, 960, 251, 61))
        self.btn_makeJson.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.event_connect(event)

    def event_connect(self, event):
        self.list_classes.itemClicked.connect(event.class_click)
        self.list_pics.itemClicked.connect(event.pic_click)
        self.btn_makeJson.clicked.connect(event.make_json)
        self.list_labels.itemClicked.connect(event.label_click)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "make sence標註檢查系統"))
        self.btn_makeJson.setText(_translate("Form", "make dataset"))


