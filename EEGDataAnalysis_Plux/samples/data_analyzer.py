import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.fft import fft, fftfreq

# Load the CSV file into a pandas DataFrame
csv_file_path = "C:\\Users\\ogoma\\CapeStone\\DataAnalyzer\\revolution-python-api\\Analog4_O2_on_our_dev\\27_11_2023__16_44_39.csv"

data = pd.read_csv(csv_file_path)

# Extracting the Sequence Number and Analog 1 data from the CSV file
sequence_number = data['Sequence Number'].values
analog_1_signal = data['Digital 4'].values
#column_array = analog_1_signal.values

print(list(analog_1_signal))
# Plotting
plt.figure(figsize=(12, 6))
plt.plot(sequence_number, analog_1_signal, label='Analog 1 Signal', color='blue')
plt.title('Analog 1 Signal vs. Sequence Number')
plt.xlabel('Sequence Number')
plt.ylabel('Analog 1 Signal')
plt.grid(True)
plt.legend()
plt.show()

