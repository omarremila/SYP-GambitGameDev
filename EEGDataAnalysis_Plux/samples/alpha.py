import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq

def calculate_frequency(data, sampling_rate):
    """Calculate the dominant frequency in the data using FFT."""
    # Convert the data to a NumPy array
    data_np = data.to_numpy()
    
    n = len(data_np)
    yf = fft(data_np)
    xf = fftfreq(n, 1 / sampling_rate)
    magnitude = 2.0/n * np.abs(yf[:n//2])
    return xf[magnitude.argmax()]
def main():
    # Load the CSV file
    file_path = 'your_file.csv'  # Replace with your actual file path
    df = pd.read_csv(file_path)

    # Extract the 'Analog 4' column
    analog_4_data = df['Analog 4']

    # Adjust the chunk size if needed
    chunk_size = 50  # Example: increased to 50

    # Other code remains the same...

if __name__ == "__main__":
    main()
