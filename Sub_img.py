from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
import SubWin_img
import UIFunctions
import Transformation as filters


# UI for gamma with paramenter slider
class Sub_img(QtWidgets.QMainWindow, SubWin_img.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self, parent=None):
        super(Sub_img, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.getDestButton)
        self.Save.clicked.connect(self.saveButton)
        self.Slider.setMinimum(1)
        self.Slider.setMaximum(100)
        self.Slider.setValue(1)
        self.Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider.setTickInterval(1)
        self.Slider.valueChanged.connect(self.gammachanged)

    def loadImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if self.fileName:
            print(self.fileName)
            pixmap = QtGui.QPixmap(self.fileName)
            self.OriginalImage.setScaledContents(True)
            self.OriginalImage.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())

    def RunBttn(self):
        try:
            self.displayProcessedIamge()
        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
        
    def saveButton(self):
        try:
            saved=self.savetofile(self.savepath,self.img,'Gamma')
            if saved:
                print('saved')
            else:
                box=QtWidgets.QMessageBox.about(self,"error","Error with save image to disk")
                print('save error')
        except:
            box=QtWidgets.QMessageBox.about(self,"error","please select directory first")
    
    def gammachanged(self):
        fvalue=self.changetofloat(self.Slider.value())
        value="Gamma value: "+ str(fvalue)
        self.ParameterLabel.setText(value)


    
    def displayProcessedIamge(self):
        input_image = self.openImage()
        self.img=self.processImage(input_image)

        #pixmap=self.covertnumpyimg(self.img)
        pixmap=self.cvImageToQImage(self.img)
        self.processed.setScaledContents(True)
        self.processed.setPixmap(pixmap)


    def processImage(self,input_image):
        self.getParameterValue()
        img=filters.Transformation().adjust_gamma(input_image,self.value)
        return img

    def openImage(self):
        input_image = cv2.imread(self.fileName)
        return input_image

    def getParameterValue(self):
        value=self.changetofloat(self.Slider.value())

        try:
            self.value = float(value)
        except:
            box=QtWidgets.QMessageBox.about(self,"Invalid number","Type a valid number")
    def changetofloat(self,value):
        fvalue=float(value)/10
        return fvalue


