import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.fft import fft, fftfreq

# Loading the data from the CSV file
csv_file_path = "C:\\Users\\ogoma\\CapeStone\\DataAnalyzer\\revolution-python-api\\Analog4_O2_on_our_dev\\27_11_2023__16_44_39.csv"
data = pd.read_csv(csv_file_path)

# Extracting the relevant channel (Analog 1) data
analog_data = data['Analog 4'].values

# Sampling rate (assumed from the script, needs to be confirmed)
sampling_rate = 1000  # Hz

# Butterworth Bandpass Filter to isolate different frequency bands
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Filtering the data for different EEG frequency bands
delta = butter_bandpass_filter(analog_data, 0.5, 4, sampling_rate)  # Delta (0.5-4 Hz)
theta = butter_bandpass_filter(analog_data, 4, 8, sampling_rate)    # Theta (4-8 Hz)
alpha = butter_bandpass_filter(analog_data, 8, 12, sampling_rate)   # Alpha (8-12 Hz)
beta = butter_bandpass_filter(analog_data, 12, 30, sampling_rate)   # Beta (12-30 Hz)
gamma = butter_bandpass_filter(analog_data, 30, 100, sampling_rate) # Gamma (30-100 Hz)

# FFT to convert the time domain signals into the frequency domain
def compute_fft(data, fs):
    N = len(data)
    T = 1.0 / fs
    yf = fft(data)
    xf = fftfreq(N, T)[:N//2]
    return xf, 2.0/N * np.abs(yf[0:N//2])

# Computing FFT for each frequency band
xf_delta, yf_delta = compute_fft(delta, sampling_rate)
xf_theta, yf_theta = compute_fft(theta, sampling_rate)
xf_alpha, yf_alpha = compute_fft(alpha, sampling_rate)
xf_beta, yf_beta = compute_fft(beta, sampling_rate)
xf_gamma, yf_gamma = compute_fft(gamma, sampling_rate)

# Plotting the Power Spectrum
plt.figure(figsize=(15, 8))

plt.subplot(5, 1, 1)
plt.plot(xf_delta, yf_delta)
plt.title('Delta Band (0.5-4 Hz) Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.subplot(5, 1, 2)
plt.plot(xf_theta, yf_theta)
plt.title('Theta Band (4-8 Hz) Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.subplot(5, 1, 3)
plt.plot(xf_alpha, yf_alpha)
plt.title('Alpha Band (8-12 Hz) Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.subplot(5, 1, 4)
plt.plot(xf_beta, yf_beta)
plt.title('Beta Band (12-30 Hz) Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.subplot(5, 1, 5)
plt.plot(xf_gamma, yf_gamma)
plt.title('Gamma Band (30-100 Hz) Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.tight_layout()
plt.show()
