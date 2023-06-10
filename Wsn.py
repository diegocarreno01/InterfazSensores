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
import RPi.GPIO as GPIO
#from __future__ import print_function
# Python imports
import http.client
import time
import urllib
from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode


# Datos
x = np.arange(1, 101, 1)
Voltajes = []
Temperatura = [ round(math.sin(xi),3) for xi in x]
Humedad = [ round(math.cos(xi),3) for xi in x]
Nivel = [xi*3.0 for xi in x]
CO2 = [random.randint(20, 50) for _ in range(100)]
LED_PIN=7


class Principal(QtWidgets.QMainWindow):
    
    def __init__ (self):
        super (Principal, self).__init__()
        uic.loadUi('Principal.ui', self)
        
        self.Button01.clicked.connect(self.function01)
        self.Button02.clicked.connect(self.function02)
        self.Button03.clicked.connect(self.function03)
        self.Button04.clicked.connect(self.function04)
        self.ON.clicked.connect(self.On)
        self.OFF.clicked.connect(self.Off)
        self.ADQUIRIR.clicked.connect(self.Adquirir)
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
        
    # Prender led->   
    def On(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)

    # Apagar led->   
    def Off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)
    
    def Adquirir(self):
        # Serial port on Raspberry Pi
        SERIAL_PORT = "/dev/ttyUSB0"  # "/dev/ttyS0"
        # BAUD rate for the XBee module connected to the Raspberry Pi
        BAUD_RATE = 9600
        # The name of the remote node (NI)
        REMOTE_NODE_ID = "SENSOR3"
        # Analog pin we want to monitor/request data
        ANALOG_LINE = IOLine.DIO3_AD3
        # Sampling rate
        SAMPLING_RATE = 15
        # Get an instance of the XBee device class
        device = XBeeDevice(SERIAL_PORT, BAUD_RATE)

        # Method to connect to the network and get the remote node by id
        def get_remote_device():
           """Get the remote node from the network 
           Returns:
           """
           # Request the network class and search the network for the remote node
           xbee_network = device.get_network()
           remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
           if remote_device is None:
              print("ERROR: Remote node id {0} not found.".format(REMOTE_NODE_ID))
              exit(1)
           remote_device.set_dest_address(device.get_64bit_addr())
           remote_device.set_io_configuration(ANALOG_LINE, IOMode.ADC)
           remote_device.set_io_sampling_rate(SAMPLING_RATE)

        def io_sample_callback(sample, remote, time):
           print("Reading from {0} at {1}:".format(REMOTE_NODE_ID, remote.get_64bit_addr()))
           # Get the temperature in Celsius
           temp_c = ((sample.get_analog_value(ANALOG_LINE) * 1200.0 / 1024.0) - 500.0) / 10.0
           # Calculate temperature in Fahrenheit
           temp_f = ((temp_c * 9.0) / 5.0) + 32.0
           print("\tTemperature is {0}C. {1}F".format(temp_c, temp_f))
           # Calculate supply voltage
           volts = (sample.power_supply_value * (1200.0 / 1024.0)) / 1000.0
           print("\tSupply voltage = {0}v".format(volts))

        try:
           print("Welcome to example of reading a remote TMP36 sensor!")
           device.open() # Open the device class
           # Setup the remote device
           get_remote_device()
           # Register a listener to handle the samples received by the local device.
           device.add_io_sample_received_callback(io_sample_callback)
           while True:
               pass
        except KeyboardInterrupt:
           if device is not None and device.is_open():
              device.close()
"""                            
    def thingspeaks(volts):
        # API KEY
        THINGSPEAK_APIKEY = '8OBA1967D0B2QS43'
        print("Welcome to the ThingSpeak Raspberry Pi temperature sensor! Press CTRL+C to stop.")
        try:
          while 1:
             # Get temperature in Celsius
             temp_c = ((500 * 3.30) - 0.5) * 10
             # Calculate temperature in Fahrenheit
             temp_f = (temp_c * 9.0 / 5.0) + 32.0
             # Display the results for diagnostics
             print("Uploading {0:.2f} C, {1:.2f} F" "".format(volts), end=' ... ')
             # Setup the data to send in a JSON (dictionary)
             params = urllib.parse.urlencode(
                  {
                     'field1': volts,
                     'field2': volts,
                     'key': THINGSPEAK_APIKEY,
                  }
             )
             # Create the header
             headers = { "Content-type": "application/x-www-form-urlencoded", 'Accept': "text/plain"}
             # Create a connection over HTTP
             conn = http.client.HTTPConnection("api.thingspeak.com:80")
             try:
                 # Execute the post (or update) request to upload the data
                 conn.request("POST", "/update", params, headers)
                 # Check response from server (200 is success)
                 response = conn.getresponse()
                 # Display response (should be 200)
                 print("Response: {0} {1}".format(response.status,response.reason))
                 # Read the data for diagnostics
                 data = response.read()
                 conn.close()
             except Exception as err:
                 print("WARNING: ThingSpeak connection failed: {0}, " "data: {1}".format(err, data))
             # Sleep for 20 seconds
             time.sleep(20)
        except KeyboardInterrupt:
             print("Thanks, bye!")
        exit(0)
"""    
    
def main():
    print("Inicia")
    app=QtWidgets.QApplication(sys.argv)
    ventana=Principal()
    ventana.show()
    sys.exit(app.exec_())


    
if __name__ == "__main__":
    main()