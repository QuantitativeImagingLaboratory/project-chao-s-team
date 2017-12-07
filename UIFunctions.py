from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# handle saving file to disk and some commone functions
class SaveFunctions:     
    def saveImagePath(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.savepath = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a directory","",options =options)
        if self.savepath:
            print(self.savepath)
            return self.savepath
        else:
            box=QtWidgets.QMessageBox.about(self,"error","Error with getting file path")
        
    def savetofile(self,path,image,type):
        output_image_name = path + "/"+type+"_"+ datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        if cv2.imwrite(output_image_name, image):
            return True
        else:
            return False
        """
    def savehisttofile(self,path,hist):
        hist_fig = plt.plot(hist)
        output_image_name = path + "/"+datetime.now().strftime("%m%d-%H%M%S")
        plt.savefig(output_image_name+"hist.png")
        """
    def savehisttofile(self,path,hist,type):
        hist_fig = plt.plot(hist)
        plt.title(type)
        output_image_name = path + "/"+datetime.now().strftime("%m%d-%H%M%S")
        plt.savefig(output_image_name+type+"hist.png")
        plt.clf()

    def savehistofile_color(self,path,hists,type):
        axes=plt.figure().gca()
        axes.set_color_cycle(['red', 'green', 'blue'])
        axes.set_title("Normalized Histogram of "+type)
        axes.plot(hists[0])
        axes.plot(hists[1])
        axes.plot(hists[2])
        output_image_name = path + "/"+datetime.now().strftime("%m%d-%H%M%S")
        plt.savefig(output_image_name+type+"hist.png")
        plt.clf()

    def getDestButton(self):
        self.savepath=self.saveImagePath()

    #convert numpy image mat to QImage 
    def cvImageToQImage(self,image):
        cvRGBImg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        qimg = QtGui.QImage(cvRGBImg.data,cvRGBImg.shape[1], cvRGBImg.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(qimg)
        return pix
    
    #convert gray scaled numpy image mat to QImage 
    def covertnumpyimg(self,image):
        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]
        image = QtGui.QImage(image, image.shape[1],image.shape[0], image.strides[0], QtGui.QImage.Format_Indexed8)
        image.setColorTable(gray_color_table)
        pix = QtGui.QPixmap(image)
        return pix

    def DisplayImage(self,labelname):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if fileName:
            print(fileName)
            pixmap = QtGui.QPixmap(fileName)
            labelname.setScaledContents(True)
            labelname.setPixmap(pixmap)
        return fileName

    def loadImage_grayscale(self,fileName):
        input_image = cv2.imread(fileName, 0)
        if input_image.dtype != 'uint8':
            box=QtWidgets.QMessageBox.about(self,"error","Please select image with type of uint8")
        return input_image

    def loadImage_color(self,fileName):
        input_image = cv2.imread(fileName)
        if input_image.dtype != 'uint8':
            box=QtWidgets.QMessageBox.about(self,"error","Please select image with type of uint8")
        return input_image


