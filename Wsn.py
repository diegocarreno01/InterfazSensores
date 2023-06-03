# -- coding: utf-8 --
"""
Created on Sat May 27 09:47:07 2023

@author: Diego
"""

#import os
import sys
import matplotlib
import numpy as np
from PyQt5 import QtWidgets, uic
#from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
import math
import random
import datetime
import Images_rc


# Datos
x = np.arange(1, 101, 1)
Temperatura = [ round(math.sin(xi),3) for xi in x]
Humedad = [ round(math.cos(xi),3) for xi in x]
Nivel = [xi*3.0 for xi in x]
CO2 = [random.randint(20, 50) for _ in range(100)]



class Principal(QtWidgets.QMainWindow):
    
    def __init__ (self):
        super (Principal, self).__init__()
        uic.loadUi('Principal.ui', self)
        
        self.Button01.clicked.connect(self.function01)
        self.Button02.clicked.connect(self.function02)
        self.Button03.clicked.connect(self.function03)
        self.Button04.clicked.connect(self.function04)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,50)
        self.tableWidget.setColumnWidth(4,50)
        self.loaddata()




    def loaddata(self):
        for i in range(0,100):
            row = i
            self.tableWidget.setRowCount(100)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem( str(datetime.datetime.now())) )
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem( str(Temperatura[i])) )
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem( str(Humedad[i])) )
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem( str(CO2[i])) )
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem( str(Nivel[i])) )
     
        
    def mostrar_grafica(self):
        fig, ax = plt.subplots()
        datos = [5, 10, 15, 20, 25]
        ax.plot(range(len(datos)), datos)
        plt.close(fig)
        
        # Guardar la figura en un archivo
        fig.savefig('grafica.png')

        # Cargar la imagen en QPixmap y mostrarla en el QLabel
        pixmap = QPixmap('grafica.png')
        self.Label01.setPixmap(pixmap)

    
    # Push Button 1 --> Al oprimirlo mostrar una gráfica.
    def function01(self):
        plt.plot(x, Temperatura, marker='o', markerfacecolor='red')
        plt.ylabel('Temperatura (°C)')
        plt.xlabel('sample')
        plt.savefig('grafica.png')
        plt.close()
        pixmap = QPixmap('grafica.png')
        self.Label01.setPixmap(pixmap)
    
    # Push Button 2 --> Al oprimirlo mostrar una gráfica con tres subplots. 
    def function02(self):
        plt.plot(x, Humedad, marker='o', markerfacecolor='red')
        plt.ylabel('Humedad del suelo (%)')
        plt.xlabel('sample')
        plt.savefig('grafica.png')
        plt.close()
        pixmap = QPixmap('grafica.png')
        self.Label01.setPixmap(pixmap)
    
    # Radio Button 1 --> Al oprimirlo mostrar una imagen en el area de trabajo.
    def function03(self):
        plt.plot(x, CO2, marker='o', markerfacecolor='red')
        plt.ylabel('Concentracion de CO2 (ppm)')
        plt.xlabel('sample')
        plt.savefig('grafica.png')
        plt.close()
        pixmap = QPixmap('grafica.png')
        self.Label01.setPixmap(pixmap)
        
    
    # Radio Button 2 -->   
    def function04(self):
        plt.plot(x, Nivel, marker='o', markerfacecolor='red')
        plt.ylabel( 'Nivel de tanque (m^3)' )
        plt.xlabel('sample')
        plt.savefig('grafica.png')
        plt.close()
        pixmap = QPixmap('grafica.png')
        self.Label01.setPixmap(pixmap)

    
    
def main():
    print("Inicia")
    app=QtWidgets.QApplication(sys.argv)
    ventana=Principal()
    ventana.show()
    sys.exit(app.exec_())


    
if __name__ == "__main__":
    main()