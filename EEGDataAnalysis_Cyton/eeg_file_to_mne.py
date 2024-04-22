import numpy as np
import mne

def read_eeg_data(file_path):
    """
    Reads EEG data from a text file, expecting each line to represent one channel.
    Each line's numerical values are extracted for MNE processing.
    """
    with open(file_path, 'r') as file:
        all_channels_data = []
        for line in file:
            # Removing characters that are not digits, minus sign or period
            sanitized_line = ''.join(c for c in line if c.isdigit() or c == '.' or c == '-' or c == ' ')
            # Splitting the sanitized string into individual strings of numbers, then converting to float
            channel_data = [float(num) for num in sanitized_line.split()]
            all_channels_data.append(channel_data)

    # Convert the list of channels into a NumPy array
    # Assuming the shape matches (n_channels, n_times) after transpose if needed
    data = np.array(all_channels_data).T  # Transposing to ensure correct shape (n_channels, n_times)
    
    return data

# Example usage
file_path = 'TimeSeriesData/2024-03-29_17-47-09_TimeSeries.txt'  # Adjust the file path
eeg_data = read_eeg_data(file_path)

# Metadata for MNE (adjust as necessary)
sampling_rate = 1000  # Hz, placeholder value
channel_names = ['Channel 1', 'Channel 2', 'Channel 3', 'Channel 4',
                 'Channel 5', 'Channel 6', 'Channel 7', 'Channel 8']  # Adjust based on your data
channel_types = ['eeg'] * len(channel_names)
info = mne.create_info(ch_names=channel_names, sfreq=sampling_rate, ch_types=channel_types)

# Create MNE RawArray
raw = mne.io.RawArray(eeg_data, info)

# Now `raw` can be used with MNE's functions
print(raw)
