import socket
import threading
import json
import numpy as np
import time

#Collects band powers in a array received from UDP connection
class BandCollector:
    def __init__(self, sleep_dur):
        self.port = 12345
        self.start_test_flag = False
        self.focus_arr = np.zeros(5)  # Assuming each incoming data array has 5 elements.
        self.lock = threading.Lock()
        self.sleep_dur = sleep_dur
        self.count = 0

    #Allows data to be collected for a specified period of time, timer_dur
    def start_test(self, timer_dur):
        with self.lock: #mutex lock 
            self.focus_arr = np.zeros(5) #reset array
            self.count = 0
            self.start_test_flag = True #data can be collected
        # Start the timer thread and end early to avoid high noise data at end of test
        threading.Timer(timer_dur - 0.1, self.end_test).start()

    #Initiate a UDP stream of data
    def start_stream(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', self.port)
        sock.bind(server_address)

        while True:  # Run indefinitely
            with self.lock:
                flag = self.start_test_flag
            if flag:  # Process data only if flag is True
                received_data, address = sock.recvfrom(4096) #Receive data from UDP socket
                try:
                    json_data = json.loads(received_data) #Data is saved in json format
                    with self.lock:
                        self.count += 1
                        self.focus_arr += np.array(json_data["data"]) #Parse the data string for only the band power data and add to array
                except json.JSONDecodeError:
                    print("Received data is not valid JSON.")
            time.sleep(self.sleep_dur)         

    #Stop collecting data
    def end_test(self):
        with self.lock:
            self.start_test_flag = False
        print("Test duration exceeded. Stopping data collection.")

    #Return EEG data array
    def getEEGData(self):
        with self.lock:
            return 100 * (self.focus_arr / self.count) # Calculate average percentage
