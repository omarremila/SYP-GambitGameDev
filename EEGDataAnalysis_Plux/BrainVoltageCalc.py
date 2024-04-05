# Constants
VCC = 3.3  # Operation Voltage in volts
GEEG = 41782  # EEG Sensor Gain
n = 16  # Number of bits of the ADC (modify this if your ADC has a different resolution)

# Function to calculate EEG voltage
def calculate_EEG_voltage(ADC_val):
    # Calculate EEG voltage based on the formula
    EEG_voltage = (((ADC_val / (2**n - 1)) - 0.5) * VCC / GEEG) * 1e6
    return EEG_voltage

# Example usage:
ADC_val = 5.420000000000000000e+02 # Example ADC value from channel A4 (modify this with your actual ADC value)
EEG_voltage = calculate_EEG_voltage(ADC_val)
print(f"The EEG voltage is: {EEG_voltage} microV")
