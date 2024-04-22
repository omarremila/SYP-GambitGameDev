import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_and_display_latest_data():
    try:
        # Load the latest row from the CSV file
        data = pd.read_csv('BandPowerPercentages.csv').iloc[-1]  # Assuming the latest data is in the last row
        categories = ['Delta', 'Theta', 'Alpha', 'Beta']
        values = [data['Delta'], data['Theta'], data['Alpha'], data['Beta']]
        
        # Clear the current chart
        ax.clear()
        
        # Create bar chart
        ax.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
        
        # Set the y-axis limit to make differences more noticeable
        ax.set_ylim(0, max(values) + 10)
        
        # Refresh the chart
        canvas.draw()
    except Exception as e:
        print(f"Error loading data: {e}")

# Create the main window
root = tk.Tk()
root.title("Brainwave Bar Chart")

# Update button
update_button = ttk.Button(root, text="Load Latest Data", command=load_and_display_latest_data)
update_button.grid(row=0, column=0, padx=10, pady=10)

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(5, 4))

# Creating a Tkinter canvas containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
