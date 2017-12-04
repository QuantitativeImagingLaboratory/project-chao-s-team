from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import SubWin_equal_UI
import UIFunctions
import Transformation as filters

# UI for gamma without paramenter
class Sub_equal(QtWidgets.QMainWindow, SubWin_equal_UI.Ui_MainWindow,UIFunctions.SaveFunctions):
    def __init__(self,parent,flag):
        super(Sub_equal, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.getDestButton)
        self.Save.clicked.connect(self.saveButton)
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

    def RunBttn(self):

        try:
            self.displayProcessedIamge()

        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
        
        #self.displayHisto_cumulative()
        #self.displayHisto_normalize()



    def saveButton(self):
        self.savehisttofile(self.savepath,self.hist_norm,'normalized')
        self.savehisttofile(self.savepath,self.hist_cum,'cumulative')
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
        input_image = self.openImage()
        self.img=self.processImage(input_image)

        pixmap=self.cvImageToQImage(self.img)
        self.processed.setScaledContents(True)
        self.processed.setPixmap(pixmap)


    def displayHisto_normalize(self):
        input_image = self.openImage()
        self.hist_norm=filters.Transformation().histogram_equalization_normalize(input_image)
        scene = QtWidgets.QGraphicsScene(self)
        #self.scene = scene
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Normalized Histogram")
        axes.plot(self.hist_norm)
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 430, 220)
        scene.addWidget(canvas)
        self.hist1.setScene(scene)

    def displayHisto_cumulative(self):
        input_image = self.openImage()
        self.hist_cum=filters.Transformation().histogram_equalization_cumulative(input_image)
        scene = QtWidgets.QGraphicsScene(self)
        #self.scene = scene
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Normalized Histogram")
        axes.plot(self.hist_cum)
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 430, 220)
        scene.addWidget(canvas)
        self.hist2.setScene(scene)


    def processImage(self,input_image):
        img=filters.Transformation().histogram_equalization_color(input_image)
        print("equal")
        return img

    def openImage(self):
        input_image = cv2.imread(self.fileName)
        print(input_image.dtype)
        return input_image

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Sub_equal(None,'equal')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()