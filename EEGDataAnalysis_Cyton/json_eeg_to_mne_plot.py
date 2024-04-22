import json
import numpy as np
import mne

# Specify the path to your data file
file_path = 'TimeSeriesData/2024-03-29_17-47-09_TimeSeries.bin'

# Load the JSON data from the binary file
with open(file_path, 'rb') as file:
    # Assuming the binary file encodes JSON data
    data = json.load(file)

# Concatenate all segments of data
# Assumes 'data' is a list of dictionaries, each with a key "data" that contains EEG data arrays
all_data = np.concatenate([segment["data"] for segment in data], axis=0)

# Define the channel names and types according to the actual EEG cap and study design
ch_names = ['CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8', 'CH9', 'CH10']
ch_types = ['eeg'] * len(ch_names)  # Assume all channels record EEG data

# Define the sampling frequency, which should match the data acquisition setup
sfreq = 250  # in Hertz

# Create an MNE Info object, which describes the EEG data layout
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

# Convert the numpy array into an MNE RawArray object for further analysis
raw = mne.io.RawArray(all_data.T, info)  # Transpose data to match MNE's expected shape

# Visualize the data
# Parameters set for quick viewing: display 5 seconds of data with auto-scaling
raw.plot(duration=5, n_channels=len(ch_names), scalings='auto')
