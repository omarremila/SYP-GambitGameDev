import pandas as pd
import matplotlib.pyplot as plt

def plot_eeg_signal(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Check if 'EEG (V)' column exists
    if 'EEG (V)' not in data.columns:
        raise ValueError("The 'EEG (V)' column is not found in the CSV file.")

    # Convert EEG values to microvolts
    data['EEG (µV)'] = data['EEG (V)'] * 1e6

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(data['EEG (µV)'], label='EEG (µV)')
    plt.xlabel('Sample Number')
    plt.ylabel('EEG Voltage (µV)')
    plt.title('EEG Signal in Microvolts')
    plt.legend()
    plt.grid(True)
    plt.show()
# Example usage
file_path = '/Users/omarg/Desktop/SYP/revolution-python-api/Analog4_O2_on_our_dev/27_11_2023__16_44_39.csv'  # Replace with the path to your CSV file
plot_eeg_signal(file_path)
