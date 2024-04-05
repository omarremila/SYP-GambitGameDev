import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bitalino import BITalino
import numpy as np

# Device setup
macAddress = "EC:1B:BD:62:F4:D9"
batteryThreshold = 30
acqChannels = [0, 1, 2, 3, 4, 5]
samplingRate = 1000
nSamples = 5
digitalOutput_on = [1, 1]
digitalOutput_off = [0, 0]

# Establish a connection to the BITalino device
device = BITalino(macAddress)
device.battery(batteryThreshold)
print(device.version())
device.start(samplingRate, acqChannels)

# Setup the plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

# Initialize the plot frame
def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(-1, 1)  # Adjust the y limits according to the expected amplitude of your signals
    return ln,

# Prepare CSV file
time_taken = datetime.datetime.now()
dt_string = time_taken.strftime("%d_%m_%Y__%H_%M_%S")
header = ["Sequence Number", "Digital 1", "Digital 2", "Digital 3", "Digital 4", "Analog 1", "Analog 2", "Analog 3", "Analog 4","Analog 5","Analog 6"]
csv_filename = f"{dt_string}.csv"
with open(csv_filename, 'w', newline='') as file:
    np.savetxt(file, [header], delimiter=",", fmt='%s')

# Animation update function
def update(frame):
    global device, nSamples, csv_filename
    samples = device.read(nSamples)
    
    # Save to CSV
    with open(csv_filename, 'a', newline='') as file:
        np.savetxt(file, samples, delimiter=",")
    
    # Plot
    y = samples[:, -1]  # Assuming we're interested in the last channel (-1 for Analog 6)
    x = frame * nSamples + np.arange(nSamples)
    xdata.extend(x)
    ydata.extend(y)
    ln.set_data(xdata, ydata)
    ax.set_xlim(x[0], x[-1] + 100)
    return ln,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(int(running_time * samplingRate / nSamples)),
                              init_func=init, blit=True)

# Show the plot
plt.show()

# Stop acquisition and close connection (this should be executed when the animation is closed)
device.trigger(digitalOutput_off)
device.stop()
device.close()
