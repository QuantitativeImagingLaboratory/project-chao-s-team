from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import cv2
from datetime import datetime
import Transformation as filters
import UIFunctions
import histColorUI

# UI for histogram
class Histogram_Color(QtWidgets.QMainWindow, histColorUI.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self, parent=None):
        super(Histogram_Color, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.getDestButton)
        self.Save.clicked.connect(self.saveButton)

    def loadImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if self.fileName:
            print(self.fileName)
            pixmap = QtGui.QPixmap(self.fileName)
            self.OriginalImage.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())

    def saveImage(self):
    	options = QtWidgets.QFileDialog.Options()
    	options |= QtWidgets.QFileDialog.DontUseNativeDialog
    	self.savepath = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a directory","",options =options)
    	if self.savepath:
    		print(self.savepath)

    def RunBttn(self):
        try:
            self.displayProcessedIamge()
        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
       

    def saveButton(self):
        try:
            saved=self.savehisttofile(self.savepath,self.hist[0],'hist_Red')
            saved=self.savehisttofile(self.savepath,self.hist[1],'hist_Green')
            saved=self.savehisttofile(self.savepath,self.hist[2],'hist_Blue')
        except:
            box=QtWidgets.QMessageBox.about(self,"error","Error with save image to disk")
    


    def displayProcessedIamge(self):
        input_image = self.openImage()
        self.hist=self.processImage(input_image)

        sceneR=self.setcanvas('Red',self.hist[0])
        self.hist1.setScene(sceneR)
        
        sceneG=self.setcanvas('Green',self.hist[1])
        self.hist2.setScene(sceneG)

        sceneB=self.setcanvas('Blue',self.hist[2])
        self.hist3.setScene(sceneB)
        

    def setcanvas(self,color,hist):
        sceneR = QtWidgets.QGraphicsScene(self)
        figureR = Figure()
        axesR = figureR.gca()
        title='Histogram '+ color
        axesR.set_title(title)
        axesR.plot(hist)
        canvasR = FigureCanvas(figureR)
        canvasR.setGeometry(0, 0, 430, 210)
        sceneR.addWidget(canvasR)
        return sceneR

    def processImage(self,input_image):
        hist=filters.Transformation().compute_histogram_color(input_image)
        return hist

    def openImage(self):
        input_image = cv2.imread(self.fileName)
        return input_image
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Histogram_Color()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
