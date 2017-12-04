from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
import SubWinNop
import UIFunctions
import Transformation as filters
import HistoMatchingUI

# UI for other
class Matching(QtWidgets.QMainWindow, HistoMatchingUI.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self,parent,flag):
        super(Matching, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.getDestButton)
        self.Save.clicked.connect(self.saveButton)
        self.imgref.clicked.connect(self.loadRefImage)
        self.type=flag

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

    def loadRefImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileNameRef, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if self.fileNameRef:
            print(self.fileNameRef)
            pixmap = QtGui.QPixmap(self.fileNameRef)
            self.imageRef.setScaledContents(True)
            self.imageRef.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())

    def RunBttn(self):
        try:
            self.displayProcessedIamge()
        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
        
    def saveButton(self):
        try:
            saved=self.savetofile(self.savepath,self.img,self.type)
            if saved:
                print('saved')
            else:
                box=QtWidgets.QMessageBox.about(self,"error","Error with save image to disk")
                print('save error')
        except:
            box=QtWidgets.QMessageBox.about(self,"error","Error with save image to disk")
    

    def displayProcessedIamge(self):
        input_image = cv2.imread(self.fileName)
        input_imageRef = cv2.imread(self.fileNameRef)
        self.img=self.processImage(input_image,input_imageRef)

        #pixmap=self.covertnumpyimg(self.img)
        pixmap=self.cvImageToQImage(self.img)
        self.processed.setScaledContents(True)
        self.processed.setPixmap(pixmap)


    def processImage(self,input_image,input_imageRef):
        img=filters.Transformation().histmatch(input_image,input_imageRef)
        print('matching')
        return img

    def openImage(self):
        input_image = cv2.imread(self.fileName, 1)
        return input_image