import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Configuration
file_path = 'FFTData/2024-03-29_17-47-09_FFT.bin'  # Path to your binary file
data_type = np.float32  # Assumed data type of your FFT data
num_points = 64  # Adjust based on how many data points per FFT

# Function to read the latest FFT data from the binary file
def read_latest_fft(file_path, num_points, data_type):
    data_size = np.dtype(data_type).itemsize * num_points  # Size of the data chunk in bytes
    try:
        with open(file_path, 'rb') as file:
            file.seek(-data_size, os.SEEK_END)  # Seek to the start of the last data chunk
            data = np.fromfile(file, dtype=data_type, count=num_points)
            return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return np.zeros(num_points)

# This function is called periodically by FuncAnimation
def update_plot(i, ax, file_path, num_points, data_type):
    fft_data = read_latest_fft(file_path, num_points, data_type)
    frequencies = np.linspace(0, 128, num_points)  # Example frequency range, adjust as needed
    
    # Clear the plot and re-plot
    ax.clear()
    ax.plot(frequencies, fft_data)
    plt.title('FFT of EEG Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)

# Setting up the plot
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_plot, fargs=(ax, file_path, num_points, data_type), interval=1000)

plt.show()
