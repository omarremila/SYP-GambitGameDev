import json
import numpy as np
import mne

# Replace 'your_data_file.bin' with the path to your actual data file
file_path = 'your_data_file.bin'

# Load the JSON data from the binary file
with open(file_path, 'rb') as f:
    data = json.load(f)

# Assuming all segments are similar and concatenating them
all_data = np.concatenate([segment["data"] for segment in data], axis=0)

# Define channel names and types (adjust according to your actual data)
ch_names = ['CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8', 'CH9', 'CH10']
ch_types = ['eeg'] * 10  # Assuming all channels are EEG

# Define the sampling frequency
sfreq = 250  # Hz, replace with your actual sampling frequency

# Create an Info object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

# Create a RawArray object
raw = mne.io.RawArray(all_data.T, info)

# Plot the data
raw.plot(duration=5, n_channels=len(ch_names), scalings='auto')
