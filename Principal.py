# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 566)
        MainWindow.setStyleSheet("background-color: rgb(139, 139, 139);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label01 = QtWidgets.QLabel(self.centralwidget)
        self.Label01.setGeometry(QtCore.QRect(10, 290, 341, 261))
        self.Label01.setStyleSheet("background-color: rgb(235, 255, 213);")
        self.Label01.setText("")
        self.Label01.setScaledContents(True)
        self.Label01.setObjectName("Label01")
        self.Button01 = QtWidgets.QPushButton(self.centralwidget)
        self.Button01.setGeometry(QtCore.QRect(50, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button01.setFont(font)
        self.Button01.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Button01.setObjectName("Button01")
        self.Button04 = QtWidgets.QPushButton(self.centralwidget)
        self.Button04.setGeometry(QtCore.QRect(50, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(10)
        self.Button04.setFont(font)
        self.Button04.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button04.setObjectName("Button04")
        self.Button03 = QtWidgets.QPushButton(self.centralwidget)
        self.Button03.setGeometry(QtCore.QRect(50, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(10)
        self.Button03.setFont(font)
        self.Button03.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button03.setObjectName("Button03")
        self.Button02 = QtWidgets.QPushButton(self.centralwidget)
        self.Button02.setGeometry(QtCore.QRect(50, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(10)
        self.Button02.setFont(font)
        self.Button02.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Button02.setObjectName("Button02")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 191, 31))
        self.textEdit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 220, 191, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 150, 191, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.textEdit_4.setObjectName("textEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(210, 10, 451, 271))
        self.tableWidget.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-top-color: rgb(0, 0, 0);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 300, 141, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Tratamiento_Imagenes/images/img04.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ON = QtWidgets.QPushButton(self.centralwidget)
        self.ON.setGeometry(QtCore.QRect(410, 420, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ON.setFont(font)
        self.ON.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 70, 46);\n"
"border-top-color: rgb(255, 255, 255);")
        self.ON.setDefault(False)
        self.ON.setObjectName("ON")
        self.OFF = QtWidgets.QPushButton(self.centralwidget)
        self.OFF.setGeometry(QtCore.QRect(530, 420, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OFF.setFont(font)
        self.OFF.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(255, 255, 255);\n"
"")
        self.OFF.setObjectName("OFF")
        self.ADQUIRIR = QtWidgets.QPushButton(self.centralwidget)
        self.ADQUIRIR.setGeometry(QtCore.QRect(440, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ADQUIRIR.setFont(font)
        self.ADQUIRIR.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);")
        self.ADQUIRIR.setObjectName("ADQUIRIR")
        self.Button01.raise_()
        self.Label01.raise_()
        self.Button04.raise_()
        self.Button03.raise_()
        self.Button02.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.textEdit_4.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.ON.raise_()
        self.OFF.raise_()
        self.ADQUIRIR.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Tratamiento_Imagenes/images/archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNuevo.setIcon(icon)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionGrafica1 = QtWidgets.QAction(MainWindow)
        self.actionGrafica1.setObjectName("actionGrafica1")
        self.actionGrafica2 = QtWidgets.QAction(MainWindow)
        self.actionGrafica2.setObjectName("actionGrafica2")
        self.actionGrafica3 = QtWidgets.QAction(MainWindow)
        self.actionGrafica3.setObjectName("actionGrafica3")
        self.actionGrafica4 = QtWidgets.QAction(MainWindow)
        self.actionGrafica4.setObjectName("actionGrafica4")
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNuevo)
        self.menuSystem.addAction(self.actionGrafica1)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionGrafica2)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionGrafica3)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionGrafica4)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(MainWindow)
        self.Button01.clicked.connect(self.Label01.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button01.setText(_translate("MainWindow", "Graficar"))
        self.Button04.setText(_translate("MainWindow", "Graficar"))
        self.Button03.setText(_translate("MainWindow", "Graficar"))
        self.Button02.setText(_translate("MainWindow", "Graficar"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">S2 --&gt; Humedad suelo (%)</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">S1 --&gt; Temperatura (°C)</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">S4 --&gt; Nivel tanque (m^3)</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">S3 --&gt; Concentración CO2</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha y hora"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "S1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "S2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "S3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S4"))
        self.ON.setText(_translate("MainWindow", "ON"))
        self.OFF.setText(_translate("MainWindow", "OFF"))
        self.ADQUIRIR.setText(_translate("MainWindow", "ADQUIRIR"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuSystem.setTitle(_translate("MainWindow", "Opciones"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionGrafica1.setText(_translate("MainWindow", "Grafica1"))
        self.actionGrafica2.setText(_translate("MainWindow", "Grafica2"))
        self.actionGrafica3.setText(_translate("MainWindow", "Grafica3"))
        self.actionGrafica4.setText(_translate("MainWindow", "Grafica4"))

import Images_rc_rc
