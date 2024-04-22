import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import random

MAX_FREQ = 48
FREQ_MESS = "Frequency (Hz)   |   Band: "

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(None)
        uic.loadUi("MindGameFreqUI.ui", self) #Load design
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.getEEGData)
    
    #Start collecting data when start button is clicked
    def start(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.timer.start(1000) #1 second
    
    #Stop collecting data when stop button is clicked
    def stop(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.timer.stop()
        #Reset GUI
        self.freqDisp1.display(0)
        self.freqDisp2.display(0)
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
        self.freq_label1.setText(FREQ_MESS)
        self.freq_label2.setText(FREQ_MESS)
    
    #Collect EEG data. Currently we have no algorithm to detect specific frequencies
    def getEEGData(self):
        self.updateBar(random.randint(0, MAX_FREQ), 1) #Random data
        self.updateBar(random.randint(0, MAX_FREQ), 2)
    
    #Update GUI with EEG data for both players
    def updateBar(self, value, player):
        if (value > MAX_FREQ):
            percent = 100
            freq = MAX_FREQ
            band = "Gamma"
        elif (value < 0):
            percent = 0
            freq = 0
            band = "Undefined"
        else:
            percent = (value / MAX_FREQ) * 100
            freq = value
            if (value < 4):
                band = "Delta"
            elif (value < 8):
                band = "Theta"
            elif (value < 12):
                band = "Alpha"
            elif (value < 30):
                band = "Beta"
            else:
                band = "Gamma"

        if player == 1: #player 1 data
            self.freqDisp1.display(freq)
            self.progressBar1.setValue(int(percent))
            self.freq_label1.setText(FREQ_MESS + band)
        else: #player 2 data
            self.freqDisp2.display(freq)
            self.progressBar2.setValue(int(percent))
            self.freq_label2.setText(FREQ_MESS + band) 
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()