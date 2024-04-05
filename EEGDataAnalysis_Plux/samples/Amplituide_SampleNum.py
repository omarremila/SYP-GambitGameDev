import matplotlib.pyplot as plt

# Let's first load the CSV file to understand its structure and contents
import pandas as pd
import numpy as np
'''
# Display the first few rows of the dataframe to understand its structure
eeg_data.head()
# Plotting the EEG data from the Analog 4 channel
plt.figure(figsize=(12, 6))
plt.plot(eeg_data['Analog 4'])
plt.title('EEG Data from Analog 4 Channel')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.show()

'''
# Load the CSV file
file_path = 'C:\\Users\\ogoma\\CapeStone\\DataAnalyzer\\revolution-python-api\\Analog4_O2_on_our_dev\\27_11_2023__16_44_39.csv'
eeg_data = pd.read_csv(file_path)




# Fast Fourier Transform (FFT) on the EEG data
fft_values = np.fft.fft(eeg_data['Analog 4'])
fft_frequencies = np.fft.fftfreq(len(fft_values), d=1)  # Assuming a sampling rate of 1 Hz for d

# Extracting positive frequencies and magnitudes for plotting
positive_frequencies = fft_frequencies[np.where(fft_frequencies >= 0)]
magnitudes = np.abs(fft_values[np.where(fft_frequencies >= 0)])

# Plotting the frequency spectrum
plt.figure(figsize=(12, 6))
plt.plot(positive_frequencies, magnitudes)
plt.title('Frequency Spectrum of EEG Data (Analog 4)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 50)  # Limiting x-axis to 50 Hz to focus on relevant EEG frequency bands
plt.show()
