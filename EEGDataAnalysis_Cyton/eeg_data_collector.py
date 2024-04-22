import socket
import threading
import json
import numpy as np
import time

class BandCollector:
    def __init__(self):
        """
        Initializes the BandCollector with a specific port and sets up the environment.
        """
        self.port = 12345  # Port number for the UDP socket
        self.start_test_flag = False  # Flag to control when data collection should occur
        self.focus_arr = np.zeros(5)  # Array to store EEG data; assumes each data array has 5 elements
        self.lock = threading.Lock()  # A lock to manage concurrent access to shared resources

    def start_test(self, timer_dur):
        """
        Starts the data collection test for a specified duration.
        
        :param timer_dur: int - Duration in seconds after which the test will stop automatically
        """
        with self.lock:
            self.focus_arr = np.zeros(5)  # Reset the EEG data array
            self.start_test_flag = True  # Enable data collection
        # Start a timer thread that will stop the test after the specified duration
        threading.Timer(timer_dur, self.end_test).start()

    def start_stream(self):
        """
        Continuously listens on the socket for incoming data and processes it if the test flag is true.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
        server_address = ('127.0.0.1', self.port)  # Server address to bind to
        sock.bind(server_address)  # Bind the socket to the server address

        while True:  # Run indefinitely to listen for incoming data
            with self.lock:
                flag = self.start_test_flag  # Check the flag status under the lock
            if flag:  # Process data only if the flag is True
                received_data, address = sock.recvfrom(4096)  # Receive data from the socket
                try:
                    json_data = json.loads(received_data)  # Try to decode the JSON data
                    with self.lock:
                        self.focus_arr += np.array(json_data["data"])  # Add the received data to the focus array
                        # Uncomment the print statement below to debug the array values in real-time
                        # print(self.focus_arr)
                except json.JSONDecodeError:
                    print("Received data is not valid JSON.")

    def end_test(self):
        """
        Stops the data collection process and logs that the test duration has been exceeded.
        """
        with self.lock:
            self.start_test_flag = False  # Set the flag to False to stop data collection
        print("Test duration exceeded. Stopping data collection.")

    def GetEEGData(self):
        """
        Retrieves the collected EEG data.
        
        :return: np.array - The collected EEG data array
        """
        with self.lock:
            return self.focus_arr.copy()  # Return a copy of the data array to avoid modification during access

# Instantiate the BandCollector
band_collector = BandCollector()
# Start the data collection thread immediately, it will run indefinitely
threading.Thread(target=band_collector.start_stream).start()
# Start a test for 10 seconds and print the data afterwards
band_collector.start_test(10)
time.sleep(10)
print(band_collector.GetEEGData())
# Start another test for 2 seconds and print the data afterwards
band_collector.start_test(2)
time.sleep(2)
print(band_collector.GetEEGData())
