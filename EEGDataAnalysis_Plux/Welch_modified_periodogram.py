import pandas as pd
import numpy as np
from scipy.signal import welch, firwin, lfilter
import matplotlib.pyplot as plt
# Use Welch's method with different parameters
nperseg = 1024  # Length of each segment (adjust based on your fs)
noverlap = 512  # Overlap between segments (usually half of nperseg)

# Load your data
df = pd.read_csv('DataCH4/27_11_2023__16_44_39_newv.csv')  # Adjust the path as necessary

# Extract specific columns
sequence_numbers = df['Sequence Number']  # Adjust column name as necessary
eeg_values = abs(df['EEG (V)'] * 1e6)  # Convert from V to µV by multiplying by 1e6

# Design the low-pass filter (assuming sampling rate is 1000 Hz, cutoff is 50 Hz)
fs = 1000  # Sampling rate
cutoff = 50  # Cutoff frequency in Hz
numtaps = 101  # Number of filter taps (filter length)
window = ('kaiser', 8.6)  # Kaiser window with beta parameter
taps = firwin(numtaps, cutoff, window=window, fs=fs)

# Apply the filter to the EEG signal data
filtered_eeg_values = lfilter(taps, 1.0, eeg_values)


frequencies, psd_values = welch(filtered_eeg_values, fs, nperseg=nperseg, noverlap=noverlap, window='hamming', average='mean')

# Use Welch's method to compute the power spectral density on the filtered data
#frequencies, psd_values = welch(filtered_eeg_values, fs, window='bandpass', nperseg=2000, noverlap=None, average='mean')

# Filter frequencies and PSD values to only include frequencies in the range 0 to 40 Hz
mask = (frequencies >= 0) & (frequencies <= 40)
filtered_frequencies = frequencies[mask]
filtered_psd_values = psd_values[mask]

# Plot the filtered power spectral density
plt.semilogy(filtered_frequencies, filtered_psd_values)
plt.title('Welch Periodogram of Filtered EEG Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [µV^2/Hz]')  # Update the label to reflect microvolts
plt.xlim(0, 40)  # This ensures that the x-axis only shows the range from 0 to 40 Hz
plt.ylim(0, 15)  # This ensures that the x-axis only shows the range from 0 to 40 Hz

plt.show()
