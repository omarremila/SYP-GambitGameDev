import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the data 
df = pd.read_csv('DataCH4/27_11_2023__16_44_39_newv.csv')

# Convert EEG (V) to EEG (µV)
df['EEG (µV)'] = abs(df['EEG (V)'] * 1000000)  # Convert from V to µV

# Select only rows 2 to 18 (note that iloc is zero-based and the end index is exclusive)
df_selected_rows = df.iloc[1:16]

# Filter the data for sequence numbers 0 to 15 within the selected rows
filtered_df = df_selected_rows[(df_selected_rows['Sequence Number'] >= 0) & (df_selected_rows['Sequence Number'] <= 15)]

# Plot the data in microvolts
plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.plot(filtered_df['Sequence Number'], filtered_df['EEG (µV)'], marker='o', linestyle='-')
plt.title('EEG (µV) vs. Sequence Number')
plt.xlabel('Sequence Number n')
plt.ylabel('EEG (µV)')
plt.grid(True)  # Add grid for better readability
plt.xticks(range(0, 16))  # Ensure x-axis ticks cover each sequence number from 0 to 15
plt.tight_layout()  # Adjust layout to make room for the labels
plt.show()


# fft


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have your filtered_df ready from the previous steps

# Your EEG signal data (assuming it's already filtered and ready for FFT analysis)
eeg_signal = filtered_df['EEG (µV)'].values

# Compute the FFT of the EEG signal
fft_result = np.fft.fft(eeg_signal)

# Compute the magnitude spectrum (amplitude for each frequency component)
magnitude_spectrum = np.abs(fft_result)

# Assuming a known sampling rate (in Hz), if not known, you'll need to estimate or find out
sampling_rate = 1000  # For example, adjust this based on your actual data

# Calculate frequency bins, considering the discrete nature of the signal
frequency_bins = np.fft.fftfreq(len(eeg_signal), d=1/sampling_rate)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.stem(frequency_bins, magnitude_spectrum, 'b', markerfmt=" ", basefmt="-b")
plt.title('FFT of EEG Signal in Discrete Time')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.tight_layout()
plt.show()
