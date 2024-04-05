import numpy as np
import os

def process_eeg_block(time_data, eeg_data, title, trial_n):
    print(time_data.shape, eeg_data.shape)
    os.makedirs("MI_trials", exist_ok=True)  # Ensure the directory exists
    np.savetxt(f"MI_trials/{title}_{trial_n}.csv", eeg_data, delimiter=",")
    return

def read_eeg_data_from_file(bin_file_path, window_size_ms, fs, n_ch):
    dtype = np.float32  # Assuming the data in the binary file is stored as float32
    trial_n = 1
    title = "eeg_trial"  # Example title, modify as needed
    
    # Load the binary data
    data = np.fromfile(bin_file_path, dtype=dtype)
    
    # Calculate the number of samples per window
    samples_per_window = int(fs * window_size_ms / 1000)
    
    # Reshape the data assuming the binary file is structured as [samples, channels]
    data = data.reshape((-1, n_ch))
    
    # Simulate timestamps for each sample based on the sampling rate
    timestamps = np.arange(data.shape[0]) / fs
    
    # Process the data in blocks
    for start_idx in range(0, data.shape[0], samples_per_window):
        end_idx = start_idx + samples_per_window
        if end_idx <= data.shape[0]:
            eeg_block = data[start_idx:end_idx, :]
            time_block = timestamps[start_idx:end_idx]
            process_eeg_block(time_block, eeg_block, title, trial_n)
            trial_n += 1

if __name__ == "__main__":
    bin_file_path = 'TimeSeriesData/2024-03-29_17-47-09_TimeSeries.bin'  # Specify the path to your binary file
    window_size_ms = 5500
    fs = 250  # Sampling frequency in Hz
    n_ch = 8  # Number of channels
    read_eeg_data_from_file(bin_file_path, window_size_ms, fs, n_ch)
