# from PyQt5 import QtWidgets, uic
 
# import sys
 
# app = QtWidgets.QApplication([])
 
# win = uic.loadUi("mainwindow_gui.ui") #specify the location of your .ui file 
# win.show()
 
# sys.exit(app.exec())


import sys
import cv2
import numpy as np

from PySide2.QtGui import QImage, QPixmap
# import PySide2.QtWidgets
# import PySide2.QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import QFile

import logging
import threading
import time
import concurrent.futures

from ui_mainwindow import Ui_MainWindow
from enum import Enum

class TypeMessage():
    def __init__(self):
        self.MESS_NOTIFY = 0
        self.MESS_WARING = 1
        self.MESS_ERROR = 2
        self.MESS_QUESTION = 3

    
class MainWindow(QMainWindow):
    filename = "automation.jpg" #path of image
    mImage = np.zeros(100).resize(10,10)          #mat mImage
    mThread = 0
    bKillThread = False

    
    def __init__(self):
        # global mImage

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #init widgets
        self.initWidgets()

        #display image
        self.filename = "automation.jpg"
        self.mImage = np.array([])
        # if self.mImage:
        #     self.display_image(self.mImage)

        #Button clicked
        self.ui.btnTest.clicked.connect(self.button_event)
        self.ui.btnGet.clicked.connect(self.button_event)
        self.ui.btnLoad.clicked.connect(self.button_event)
        #Checkbox
        self.ui.cbTest.clicked.connect(self.button_event)
        #radiobox
        self.ui.rdTest.clicked.connect(self.button_event)

        #Slider
        self.ui.sldTest.valueChanged.connect(self.slider_event)

        #combobox
        self.ui.cbbTest.currentTextChanged.connect(self.cbb_event)

        #tab
        self.ui.tabWidget.currentChanged.connect(self.tabwidget_event)
        

    def thread_function(self, name):
        for i in range(100):
            if self.bKillThread:
                break
            print("Thread {0}: finishing- {1}".format(name, i))
            time.sleep(0.05)
        print("finish thread")


    def closeEvent(self, event): 
        event.ignore();
        print ("Closing") 
        result = self.show_messagebox(TypeMessage().MESS_QUESTION,"Are you sure exit program")
        if result == QMessageBox.Yes:
            event.accept();
        else:
            return
        

    def initWidgets(self):
        ''' Init all widgets '''
        self.ui.lbImg.setScaledContents(True)

        
        # QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function)
        # self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent )
        # self.mThread = threading.Thread(target=self.thread_function, args=(1,),daemon=True)

    def button_event(self):
        ''' Button clicked event '''
        if self.sender() == self.ui.btnTest:
            self.ui.lb_btnStatus.setText("test clicked")
            self.mThread = threading.Thread(target=self.thread_function, args=(1,),daemon=True)
            print("...Start thread...")
            self.bKillThread = False
            self.mThread.start()
            # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            #     executor.map(self.thread_function, range(3))
            self.ui.lb_btnStatus.setText("done")

        elif self.sender() == self.ui.btnGet:
            data = self.ui.edtTest.text()
            print(data)
            self.bKillThread = True
            print("...Stop thread...")

        #btn Load    
        elif self.sender() == self.ui.btnLoad:
            self.filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
            print("Path of image = ", self.filename)
            if self.filename == "":
                self.ui.edtPath.setText("null")
                return
            elif (self.filename.find(".jpg") != -1) or (self.filename.find(".png") != -1) or (self.filename.find(".bmp") != -1):
                self.ui.edtPath.setText(self.filename)
                self.mImage = cv2.imread(self.filename)
                self.display_image(self.mImage)

        elif self.sender() == self.ui.cbTest:
            self.ui.lb_checkboxStaus.setText(str(self.ui.cbTest.isChecked()))
        elif self.sender() == self.ui.rdTest:
            self.ui.lb_radioStatus.setText(str(self.ui.rdTest.isChecked()))

    def slider_event(self):
        ''' Slider change event '''
        if self.sender() == self.ui.sldTest:
            self.ui.lb_sldVal.setText(str(self.ui.sldTest.value()))
    
    def cbb_event(self):
        ''' combobox change event '''
        if self.sender() == self.ui.cbbTest:
            self.ui.lb_cbbStatus.setText(self.ui.cbbTest.currentText())
            print("index = ",self.ui.cbbTest.currentIndex() )
            self.show_messagebox(self.ui.cbbTest.currentIndex(),self.ui.cbbTest.currentText())
    
    def tabwidget_event(self):
        ''' tabWidget change event '''
        if self.sender() == self.ui.tabWidget:
            self.ui.lb_tabVal.setText(str(self.ui.tabWidget.currentIndex()))
            print("tab index = ",self.ui.tabWidget.currentIndex() )


    def display_image(self, image):
        ''' Display a image on lable'''
        size = image.shape
        step = image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.ui.lbImg.setPixmap(QPixmap.fromImage(img))

    def show_messagebox(self, mes_type = 0, mes_infor = "Message box"):
        ''' show messagebox '''
        msg = QMessageBox()
        # msg.setGeometry(500,500,900,900)
        if mes_type == TypeMessage().MESS_NOTIFY:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Notify")
            msg.setText(mes_infor)
            msg.setStandardButtons(QMessageBox.Ok)

        elif mes_type == TypeMessage().MESS_WARING:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Warning, please carefully!")
            msg.setInformativeText(mes_infor)
            msg.setStandardButtons(QMessageBox.Ok)

        elif mes_type == TypeMessage().MESS_ERROR:
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Error, try to fix")
            msg.setDetailedText(mes_infor)
            msg.setStandardButtons(QMessageBox.Ok)

        elif mes_type == TypeMessage().MESS_QUESTION:
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Question?")
            msg.setText("Select your anwser!")            
            msg.setInformativeText(mes_infor)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        msg.buttonClicked.connect(self.msgbtn)
        retval = msg.exec_()
        print ("value of pressed message box button: ", retval)
        return retval

    
    def msgbtn(self,i):
        print ("Button pressed is:",i.text())    
        

if __name__ == "__main__":
    print("****************************")
    print("**********Main**************")
    print("****************************")
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Hello world!")
    window.show()

    sys.exit(app.exec_())