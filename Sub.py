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

# UI for histogram
class Sub(QtWidgets.QMainWindow, SubWin.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Sub, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.saveImage)

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


    def displayProcessedIamge(self):
        input_image = self.openImage()
        hist=self.processImage(input_image)
        scene = QtWidgets.QGraphicsScene(self)
        self.scene = scene
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Histogram")
        axes.plot(hist)
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 440, 460)
        scene.addWidget(canvas)
        self.graphicsView.setScene(scene)

    def processImage(self,input_image):
        hist=filters.Transformation().compute_histogram(input_image)
        return hist

    def openImage(self):
        input_image = cv2.imread(self.fileName, 0)
        return input_image

    def save(self,path,image):
        output_image_name = path + "/Histogram" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, image)
        
        





def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Sub()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()





