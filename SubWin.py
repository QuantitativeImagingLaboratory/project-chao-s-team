# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImage.setMaximumSize(QtCore.QSize(449, 469))
        self.OriginalImage.setScaledContents(True)
        self.OriginalImage.setObjectName("OriginalImage")
        self.gridLayout.addWidget(self.OriginalImage, 0, 0, 1, 1)
        self.destination = QtWidgets.QPushButton(self.centralwidget)
        self.destination.setObjectName("destination")
        self.gridLayout.addWidget(self.destination, 2, 0, 1, 1)
        self.origImage = QtWidgets.QPushButton(self.centralwidget)
        self.origImage.setObjectName("origImage")
        self.gridLayout.addWidget(self.origImage, 1, 0, 1, 1)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 1, 1, 1, 1)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 2, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMaximumSize(QtCore.QSize(449, 469))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 22))
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
        self.OriginalImage.setText(_translate("MainWindow", "TextLabel"))
        self.destination.setText(_translate("MainWindow", "Select Directory to Save Transformed Image"))
        self.origImage.setText(_translate("MainWindow", "Select Image"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Save.setText(_translate("MainWindow", "Save"))

