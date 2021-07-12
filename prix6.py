# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prix6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 621, 431))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Factor O3</span></p><p><span style=\" font-size:10pt;\">El factor O3 tiene en cuenta las condiciones del proceso y es una medida de la cantidad de sustancia en fase gaseosa tras su liberación, entonces según la siguiente tabla del libro purpura: </span></p><p><span style=\" font-size:10pt; color:#000000;\">X = 4.5 × </span><span style=\" font-size:10pt; font-style:italic; color:#000000;\">Psat </span><span style=\" font-size:10pt; color:#000000;\">– 3.5</span></p><p><span style=\" font-size:10pt;\">Pi es igual a la presión parcial de vapor (en bares) de la sustancia a la temperatura del proceso </span></p><p><br/></p><table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\"><tr><td width=\"294\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-weight:600;\">Fase</span></p></td><td width=\"55\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-weight:600;\">O3</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Gas </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>10 </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Liquido con presión de saturación a la temperatura del proceso de 3 bares o más </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>10 </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Liquido con presión de saturación a la temperatura del proceso entre 1 a 3 bares </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p> X+Δ     </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Liquido con presión de saturación a la temperatura del proceso menor de 1 bar </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Pi + <span style=\" font-family:\'arial,sans-serif\'; font-size:16px; color:#202124; background-color:#ffffff;\">Δ</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Solido </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>0.1 </p></td></tr></table><p><br/></p><table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\"><tr><td width=\"151\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-weight:600;\">Condiciones</span></p></td><td width=\"28\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><img src=\"file:///C:/Users/oscar/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"9\" height=\"19\" style=\"vertical-align: top;\"/></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>-25°C &lt; Tbp </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>0 </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>-75°C &lt; Tbp &lt; -25 °C </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>1 </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>-125°C &lt; Tbp &lt; -75°C </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>2 </p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>Tbp &lt; -125°C </p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p>3 </p></td></tr></table><p><br/></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Cerrar"))




