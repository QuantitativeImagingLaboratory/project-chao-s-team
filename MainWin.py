# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 185, 229))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Negative = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Negative.setObjectName("Negative")
        self.verticalLayout.addWidget(self.Negative)
        self.Log = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Log.setObjectName("Log")
        self.verticalLayout.addWidget(self.Log)
        self.Gamma = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Gamma.setObjectName("Gamma")
        self.verticalLayout.addWidget(self.Gamma)
        self.Histogram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Histogram.setObjectName("Histogram")
        self.verticalLayout.addWidget(self.Histogram)
        self.Equalization = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Equalization.setObjectName("Equalization")
        self.verticalLayout.addWidget(self.Equalization)
        self.Shaping = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Shaping.setObjectName("Shaping")
        self.verticalLayout.addWidget(self.Shaping)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Intensity Transformation"))
        self.Negative.setText(_translate("MainWindow", "Image Negatives"))
        self.Log.setText(_translate("MainWindow", "Log Transformation"))
        self.Gamma.setText(_translate("MainWindow", "Gamma Transformation"))
        self.Histogram.setText(_translate("MainWindow", "Histogram"))
        self.Equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.Shaping.setText(_translate("MainWindow", "Histogram Matching"))

