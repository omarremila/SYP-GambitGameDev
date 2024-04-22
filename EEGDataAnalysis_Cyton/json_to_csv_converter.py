import pandas as pd
import json

# Function to read N lines from the file starting from a specific line
# Increase the display precision for floating-point numbers
pd.set_option('display.precision', 9)

def read_n_lines(file_name, start_line, n=50):
    lines = []
    with open(file_name, 'r') as file:
        # Skip to the start_line
        for _ in range(start_line):
            next(file)
        # Read the next n lines
        for _ in range(n):
            line = file.readline()
            if not line:
                break  # End of file reached
            lines.append(line)
    return lines

# Updated processing function
def process_and_save_to_csv(file_name, n=1, total_lines=600):
    start_line = 50
    percentages_list = []

    while start_line < total_lines:
        data = read_n_lines(file_name, start_line, n)
        records = []
        for line in data:
            try:
                record = json.loads(line)
                records.append(record)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue  # Skip lines that cause JSON decoding errors

        if records:
            df = pd.DataFrame([record['data'] for record in records], columns=['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma'])

            # Write the DataFrame to CSV file outside the loop
            df.to_csv('BandPower_10hz.csv', mode='a', index=False, header=not start_line)  # Append mode and avoid writing headers for each iteration

        start_line += n

# Call the function to process and save to CSV
process_and_save_to_csv('OpenBCI_LSL/BandPassData/BandPower_10_acurret.json')
