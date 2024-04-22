import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import random
import collecting_bands
import threading
import numpy as np


displayLen = 200 #milliseconds

#Updates GUI with average band powers
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(None)
        uic.loadUi("MindGameBandPowerUI.ui", self) #Load design
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)
        #time processing thread sleeps.
        self.sleep_dur = 0.01
        #Create instance of band collection
        self.band_collector = collecting_bands.BandCollector(self.sleep_dur)
        # Start the data collection thread immediately, it will run indefinitely
        threading.Thread(target=self.band_collector.start_stream).start()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.getData)
        self.stopTimer = QtCore.QTimer(self)
        self.stopTimer.timeout.connect(self.stop)
    
    #Start collecting data when start button is clicked
    def start(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        #Reset GUI
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
        self.progressBar3.setValue(0)
        self.progressBar4.setValue(0)
        self.progressBar5.setValue(0)
        self.band_collector.start_test(self.durationBox.value())
        self.timer.start(displayLen)
        self.stopTimer.start(self.durationBox.value()*1000)
    
    #Stop collecting data when stop button is clicked
    def stop(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.timer.stop()
        self.stopTimer.stop()
    
    #Collect EEG data from processing thread
    def getData(self):
        self.updateBar(self.band_collector.getEEGData()) #Random data
    
    #Update GUI with EEG for each band
    def updateBar(self, value):
        self.progressBar1.setValue(int(value[0]))
        self.progressBar2.setValue(int(value[1]))
        self.progressBar3.setValue(int(value[2]))
        self.progressBar4.setValue(int(value[3]))
        self.progressBar5.setValue(int(value[4]))

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()