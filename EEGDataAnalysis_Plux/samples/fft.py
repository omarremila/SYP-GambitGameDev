import numpy as np
import matplotlib.pyplot as plt

# Example signal data (replace this with your actual data)
amplitudes = np.array([your_amplitude_data])  # Replace with your amplitude data
sample_numbers = np.array([your_sample_numbers])  # Replace with your sample numbers

# Calculate the time between each sample (inverse of the sampling rate)
sampling_rate = 1000  # Replace with your actual sampling rate in Hz
dt = 1 / sampling_rate

# Apply FFT to the signal
fft_result = np.fft.fft(amplitudes)

# Compute the frequency bins
n = len(amplitudes)
frequencies = np.fft.fftfreq(n, dt)

# Plot the frequency spectrum
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:n // 2], np.abs(fft_result)[:n // 2])  # Plot only the positive frequencies
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

# Find the peak frequency
peak_frequency = frequencies[np.argmax(np.abs(fft_result))]
print(f"The peak frequency is: {peak_frequency} Hz")
