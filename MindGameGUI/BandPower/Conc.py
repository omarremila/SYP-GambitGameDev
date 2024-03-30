import sys
import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import time

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress_updated = QtCore.pyqtSignal(dict)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def work(self):
        try:
            # Load the last row of the CSV file as the latest data
            data = pd.read_csv(self.filename).iloc[-1].to_dict()
            self.progress_updated.emit(data)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        finally:
            self.finished.emit()
        time.sleep(1)  # Simulate work

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MindGame.ui", self)  # Load the design
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)

    def start(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        # Specify the correct path to your CSV file
        self.worker = Worker("BandPowerPercentages.csv")
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.work)
        self.worker.progress_updated.connect(self.updateBars)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.start()

    def stop(self):
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def updateBars(self, data):
        # Assuming you have progress bars named accordingly in your UI
        self.progressBarDelta.setValue(data.get('Delta', 0))
        self.progressBarTheta.setValue(data.get('Theta', 0))
        self.progressBarAlpha.setValue(data.get('Alpha', 0))
        self.progressBarBeta.setValue(data.get('Beta', 0))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
