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
        return savepath
        
    def savetofile(self,path,image,type):
        output_image_name = path + "/"+type+"_"+ datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        if cv2.imwrite(output_image_name, image):
            return True
        else:
            return False
    def savehisttofile(self,path,hist):
        hist_fig = plt.plot(hist)
        output_image_name = path + "/"
        plt.savefig(output_image_name+"hist.png")
        
    def getDestButton(self):
        self.savepath=self.saveImagePath()

