# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sliders.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RGB Colour Picker")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.redSlider = QtWidgets.QSlider(self.centralwidget)
        self.redSlider.setGeometry(QtCore.QRect(170, 150, 51, 201))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Vertical)
        self.redSlider.setInvertedAppearance(True)
        self.redSlider.setObjectName("redSlider")
        self.greenSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenSlider.setGeometry(QtCore.QRect(360, 150, 51, 201))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Vertical)
        self.greenSlider.setInvertedAppearance(True)
        self.greenSlider.setObjectName("greenSlider")
        self.blueSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueSlider.setGeometry(QtCore.QRect(560, 150, 51, 201))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Vertical)
        self.blueSlider.setInvertedAppearance(True)
        self.blueSlider.setObjectName("blueSlider")
        self.showValue = QtWidgets.QLabel(self.centralwidget)
        self.showValue.setGeometry(QtCore.QRect(290, 430, 231, 81))
        self.showValue.setObjectName("showValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getValues(self):
        self.redSlider.value

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showValue.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
