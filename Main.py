from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainWin
import Sub
from Sub_img import Sub_img
from SubWin_img_nopa import Sub_img_nopa
from SubWin_equal import Sub_equal



class Main(QtWidgets.QMainWindow, MainWin.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.Negative.clicked.connect(self.negative)
        self.Log.clicked.connect(self.log)
        self.Histogram.clicked.connect(self.openSubWin)
        self.Equalization.clicked.connect(self.equal)
        self.Shaping.clicked.connect(self.matching)
        self.Gamma.clicked.connect(self.openSubWin_img)

    #histogram
    def openSubWin(self):
    	Sub.Sub(self).show()
    
    #gamma 
    def openSubWin_img(self):
        Sub_img(self).show()
    #negative
    def negative(self):
        Sub_img_nopa(self,'neg').show()

    def log(self):
        Sub_img_nopa(self,'log').show()

    def equal(self):
        Sub_equal(self,'equal').show()
        
    def matching(self):
        Sub_img_nopa(self,'matching').show()

   
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()