# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\_aaa\py_qt\mainwindow_gui.ui',
# licensing of 'D:\_aaa\py_qt\mainwindow_gui.ui' applies.
#
# Created: Wed May 29 14:35:22 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Speed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setGeometry(QtCore.QRect(20, 10, 93, 36))
        self.btnTest.setObjectName("btnTest")
        self.cbTest = QtWidgets.QCheckBox(self.centralwidget)
        self.cbTest.setGeometry(QtCore.QRect(25, 65, 81, 20))
        self.cbTest.setObjectName("cbTest")
        self.rdTest = QtWidgets.QRadioButton(self.centralwidget)
        self.rdTest.setGeometry(QtCore.QRect(25, 115, 95, 20))
        self.rdTest.setObjectName("rdTest")
        self.lb_btnStatus = QtWidgets.QLabel(self.centralwidget)
        self.lb_btnStatus.setGeometry(QtCore.QRect(125, 15, 121, 26))
        self.lb_btnStatus.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_btnStatus.setObjectName("lb_btnStatus")
        self.edtPath = QtWidgets.QLineEdit(self.centralwidget)
        self.edtPath.setGeometry(QtCore.QRect(270, 250, 196, 22))
        self.edtPath.setObjectName("edtPath")
        self.cbbTest = QtWidgets.QComboBox(self.centralwidget)
        self.cbbTest.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.cbbTest.setObjectName("cbbTest")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbbTest.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icon/2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbbTest.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icon/3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbbTest.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icon/4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbbTest.addItem(icon4, "")
        self.sldTest = QtWidgets.QSlider(self.centralwidget)
        self.sldTest.setGeometry(QtCore.QRect(30, 180, 160, 19))
        self.sldTest.setMaximum(100)
        self.sldTest.setOrientation(QtCore.Qt.Horizontal)
        self.sldTest.setObjectName("sldTest")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 330, 181, 211))
        self.tabWidget.setObjectName("tabWidget")
        self.tabAuto = QtWidgets.QWidget()
        self.tabAuto.setObjectName("tabAuto")
        self.lbAuto = QtWidgets.QLabel(self.tabAuto)
        self.lbAuto.setGeometry(QtCore.QRect(25, 20, 55, 16))
        self.lbAuto.setObjectName("lbAuto")
        self.tabWidget.addTab(self.tabAuto, "")
        self.tabManual = QtWidgets.QWidget()
        self.tabManual.setObjectName("tabManual")
        self.lbManual = QtWidgets.QLabel(self.tabManual)
        self.lbManual.setGeometry(QtCore.QRect(35, 25, 55, 16))
        self.lbManual.setObjectName("lbManual")
        self.tabWidget.addTab(self.tabManual, "")
        self.lbImg = QtWidgets.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(205, 285, 571, 271))
        self.lbImg.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lbImg.setText("")
        self.lbImg.setObjectName("lbImg")
        self.lb_checkboxStaus = QtWidgets.QLabel(self.centralwidget)
        self.lb_checkboxStaus.setGeometry(QtCore.QRect(125, 60, 121, 26))
        self.lb_checkboxStaus.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_checkboxStaus.setObjectName("lb_checkboxStaus")
        self.lb_radioStatus = QtWidgets.QLabel(self.centralwidget)
        self.lb_radioStatus.setGeometry(QtCore.QRect(125, 110, 121, 26))
        self.lb_radioStatus.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_radioStatus.setObjectName("lb_radioStatus")
        self.lb_tabVal = QtWidgets.QLabel(self.centralwidget)
        self.lb_tabVal.setGeometry(QtCore.QRect(10, 295, 121, 26))
        self.lb_tabVal.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_tabVal.setObjectName("lb_tabVal")
        self.lb_sldVal = QtWidgets.QLabel(self.centralwidget)
        self.lb_sldVal.setGeometry(QtCore.QRect(200, 175, 46, 26))
        self.lb_sldVal.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_sldVal.setObjectName("lb_sldVal")
        self.lb_cbbStatus = QtWidgets.QLabel(self.centralwidget)
        self.lb_cbbStatus.setGeometry(QtCore.QRect(400, 15, 121, 26))
        self.lb_cbbStatus.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(170, 0, 0);\n"
"border-radius: 5px;")
        self.lb_cbbStatus.setObjectName("lb_cbbStatus")
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(205, 250, 61, 26))
        self.btnLoad.setObjectName("btnLoad")
        self.edtTest = QtWidgets.QLineEdit(self.centralwidget)
        self.edtTest.setGeometry(QtCore.QRect(400, 50, 116, 22))
        self.edtTest.setObjectName("edtTest")
        self.btnGet = QtWidgets.QPushButton(self.centralwidget)
        self.btnGet.setGeometry(QtCore.QRect(270, 50, 126, 26))
        self.btnGet.setObjectName("btnGet")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btnTest.setText(QtWidgets.QApplication.translate("MainWindow", "button", None, -1))
        self.cbTest.setText(QtWidgets.QApplication.translate("MainWindow", "CheckBox", None, -1))
        self.rdTest.setText(QtWidgets.QApplication.translate("MainWindow", "RadioButton", None, -1))
        self.lb_btnStatus.setText(QtWidgets.QApplication.translate("MainWindow", "Button Status", None, -1))
        self.cbbTest.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Model 1", None, -1))
        self.cbbTest.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Model 2", None, -1))
        self.cbbTest.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Model 3", None, -1))
        self.cbbTest.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Model 4", None, -1))
        self.lbAuto.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAuto), QtWidgets.QApplication.translate("MainWindow", "Auto", None, -1))
        self.lbManual.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManual), QtWidgets.QApplication.translate("MainWindow", "Manual", None, -1))
        self.lb_checkboxStaus.setText(QtWidgets.QApplication.translate("MainWindow", "Check box status", None, -1))
        self.lb_radioStatus.setText(QtWidgets.QApplication.translate("MainWindow", "Radio status", None, -1))
        self.lb_tabVal.setText(QtWidgets.QApplication.translate("MainWindow", "Tab Status", None, -1))
        self.lb_sldVal.setText(QtWidgets.QApplication.translate("MainWindow", "Radio status", None, -1))
        self.lb_cbbStatus.setText(QtWidgets.QApplication.translate("MainWindow", "Combobox Status", None, -1))
        self.btnLoad.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.btnGet.setText(QtWidgets.QApplication.translate("MainWindow", "Get", None, -1))

import Icon_rc
