import pandas as pd
import numpy as np

# Assuming the CSV data is stored in "data.csv"
file_path = 'BandPower_10hz.csv'  # Update this to your actual file path

# Load the CSV data into a DataFrame
df = pd.read_csv(file_path, header=None)
df.columns = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']

# Normalize the data if necessary
# Here we ensure all values are ≤ 0.8
df = df / df.max().max() * 0.8

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup the plot
fig, ax = plt.subplots()
bars = plt.bar(df.columns, df.iloc[0])

# Update function for the animation
"""
    Update function for the bar chart animation which adjusts the heights
    of the bars to new data points.
"""
def update(frame):
    for bar, height in zip(bars, df.iloc[frame]):
        bar.set_height(height)
    return bars

# Create the animation
ani = FuncAnimation(fig, update, frames=len(df), blit=True, repeat=False)

plt.show()
