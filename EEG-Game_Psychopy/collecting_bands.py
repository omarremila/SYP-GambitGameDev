import socket
import threading
import json
import numpy as np
import time

class BandCollector:
    def __init__(self, sleep_dur):
        self.port = 12345
        self.start_test_flag = False
        self.focus_arr = np.zeros(5)  # Assuming each incoming data array has 5 elements.
        self.lock = threading.Lock()
        self.sleep_dur = sleep_dur

    def start_test(self, timer_dur):
        with self.lock:
            self.focus_arr = np.zeros(5)
            self.start_test_flag = True
        # Start the timer thread
        #print("start")
        threading.Timer(timer_dur - 0.5, self.end_test).start()

    def start_stream(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', self.port)
        sock.bind(server_address)

        while True:  # Run indefinitely
            with self.lock:
                flag = self.start_test_flag
            if flag:  # Process data only if flag is True
                received_data, address = sock.recvfrom(4096)
                try:
                    json_data = json.loads(received_data)
                    with self.lock:
                        self.focus_arr += np.array(json_data["data"])
                        #print(self.focus_arr)
                except json.JSONDecodeError:
                    print("Received data is not valid JSON.")
            time.sleep(self.sleep_dur)
            

    def end_test(self):
        with self.lock:
            self.start_test_flag = False
        print("Test duration exceeded. Stopping data collection.")

    def getEEGData(self):
        with self.lock:
            print(self.focus_arr)
            return self.focus_arr
