import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore
from MindGame_ui import Ui_MainWindow  # Ensure this matches the generated Python file from your UI

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress_updated = QtCore.pyqtSignal(dict)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def work(self):
        try:
            data = pd.read_csv(self.filename).iloc[-1].to_dict()
            self.progress_updated.emit(data)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        finally:
            self.finished.emit()
        QtCore.QThread.sleep(1)  # Simulate work for demonstration

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load the UI
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)

    def start(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.worker = Worker("BandPowerPercentages.csv")  # Specify the correct CSV file path
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.work)
        self.worker.progress_updated.connect(self.updateBars)  # Connect signal to the slot
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
        # Update the progress bars with the received data
        self.progressBarDelta.setValue(data.get('Delta', 0))
        self.progressBarTheta.setValue(data.get('Theta', 0))
        self.progressBarAlpha.setValue(data.get('Alpha', 0))
        self.progressBarBeta.setValue(data.get('Beta', 0))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
