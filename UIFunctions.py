from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
# handle saving file to disk
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


