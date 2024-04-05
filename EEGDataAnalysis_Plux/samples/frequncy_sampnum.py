import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def plot_eeg_frequency_domain(file_path, sampling_rate):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Check if 'EEG (V)' column exists
    if 'EEG (V)' not in data.columns:
        raise ValueError("The 'EEG (V)' column is not found in the CSV file.")

    # EEG signal in volts, converted to a NumPy array
    eeg_signal = data['EEG (V)'].to_numpy()

    # Check if the signal is valid
    if np.isnan(eeg_signal).all() or len(eeg_signal) == 0:
        raise ValueError("The EEG signal is empty or invalid.")

    # Number of sample points
    N = len(eeg_signal)
    # Sample spacing
    T = 1.0 / sampling_rate

    # FFT
    eeg_fft = fft(eeg_signal)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

    # Plotting the Frequency Domain representation
    plt.figure(figsize=(12, 6))
    plt.plot(xf, 2.0/N * np.abs(eeg_fft[:N//2]))
    plt.xscale('log')  # Using logarithmic scale for x-axis
    plt.yscale('log')  # Using logarithmic scale for y-axis
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain Representation of EEG Signal')
    plt.grid(True)
    plt.show()
# Example usage
file_path = '/Users/omarg/Desktop/SYP/revolution-python-api/Analog4_O2_on_our_dev/27_11_2023__16_44_39.csv'  # Replace with the path to your CSV file
sampling_rate = 1000  # Replace with your actual sampling rate
plot_eeg_frequency_domain(file_path, sampling_rate)
