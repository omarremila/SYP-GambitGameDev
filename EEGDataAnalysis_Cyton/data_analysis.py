import json
import threading
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import queue

# Mock input data string
all_data = """
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}
{"type":"averageBandPower","data":[1,1,1,1,1]}"""  # Keep your data string as it is.

# Thread-safe queue for inter-thread communication
data_queue = queue.Queue()

def producer():
    for line in all_data.strip().splitlines():
        json_data = json.loads(line)
        data_queue.put(json_data['data'])
        time.sleep(0.1)  # Simulate time delay

def start_animation(input_data):
    def animate(i):
        if not input_data:
            return
        # Normalize and update plot
        max_value = np.max(input_data)
        normalized_array = np.array(input_data) / max_value * 1
        if i < len(normalized_array):
            for bar, height in zip(bars, normalized_array[i]):
                bar.set_height(height)
            frame_text.set_text(f'Frame: {i+1}/{len(input_data)}')

    # Setup plot
    fig, ax = plt.subplots()
    plt.style.use('dark_background')
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')
    bands = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars = plt.bar(bands, [0, 0, 0, 0, 0], color=colors, edgecolor='white')
    ax.set_title('Band Power Over Time', color='white', fontsize=16, fontweight='bold')
    ax.set_xlabel('Frequency Band', color='white', fontsize=14)
    ax.set_ylabel('Normalized Power', color='white', fontsize=14)
    plt.xticks(color='white', fontsize=12)
    plt.yticks(color='white', fontsize=12)
    frame_text = ax.text(0.95, 0.95, '', transform=ax.transAxes, color='white', horizontalalignment='right', verticalalignment='top')

    # Set y-axis limits
    ax.set_ylim([0, 1])
    
    ani = FuncAnimation(fig, animate, frames=len(input_data), blit=False, repeat=False)
    plt.show()

def main():
    # Input data list for animation
    input_data = []

    # Start producer thread
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # Main thread loop to update plot
    try:
        while producer_thread.is_alive() or not data_queue.empty():
            try:
                # Try to get data from the queue without blocking
                data = data_queue.get(block=False)
                input_data.append(data)
            except queue.Empty:
                # No data available, yield control
                time.sleep(0.1)
        # Start the animation with the collected data
        start_animation(input_data)
    finally:
        producer_thread.join()

if __name__ == "__main__":
    main()
