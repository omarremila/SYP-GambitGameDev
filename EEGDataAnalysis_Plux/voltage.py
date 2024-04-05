import pandas as pd

def add_eeg_column(file_path, output_path):
    # Constants for the formula
    V_CC = 3.3  # Operation Voltage in Volts
    G_EEG = 41782  # EEG Sensor Gain
    n = 12  # Number of bits of the channel (assumed)

    # Load the CSV file
    data = pd.read_csv(file_path)

    # Calculate the EEG (V) column
    data['EEG (V)'] = ( ((data['Analog 4'] / (2**n ))- 0.5) * V_CC) / G_EEG

    # Create a new DataFrame with only 'Sequence Number' and 'EEG (V)'
    output_data = data[['Sequence Number', 'EEG (V)']]

    # Save the new DataFrame to a new CSV file
    output_data.to_csv(output_path, index=False)
    print(f"File saved as '{output_path}'")


# Example usage
file_path = '/Users/omarg/Desktop/SYP-GambitGameDev/Data_Analysis/DataCH4/27_11_2023__16_44_39.csv'  # Replace with the path to your input CSV file
output_path = '/Users/omarg/Desktop/SYP-GambitGameDev/Data_Analysis/DataCH4/27_11_2023__16_44_39_newv.csv'  # Replace with the desired path for the output CSV file
add_eeg_column(file_path, output_path)
