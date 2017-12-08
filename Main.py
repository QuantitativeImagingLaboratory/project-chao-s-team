from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainWin
import Sub
from Sub_img import Sub_img
from SubWin_img_nopa import Sub_img_nopa
from SubWin_equal import Sub_equal
from SubWin_equal_color import Sub_equal_color
from Histogram_Color import Histogram_Color
from Matching import Matching


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
        self.histogram_color.clicked.connect(self.histogramColor)
        self.Equalization_color.clicked.connect(self.equal_color)

    #histogram grayscale
    def openSubWin(self):
    	Sub.Sub(self).show()
    #histgram color
    def histogramColor(self):
        Histogram_Color(self).show()
    #gamma 
    def openSubWin_img(self):
        Sub_img(self).show()
    #negative
    def negative(self):
        Sub_img_nopa(self,'neg').show()
    #logarithmic 
    def log(self):
        Sub_img_nopa(self,'log').show()
    #equalization grayscale
    def equal(self):
        Sub_equal(self,'equal').show()
    #equalization color
    def equal_color(self):
        Sub_equal_color(self,'equal_color').show()
    # histogram matching
    def matching(self):
        Matching(self,'matching').show()
    

   
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()