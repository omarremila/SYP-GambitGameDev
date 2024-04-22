import socket
import threading
import json
import numpy as np
import time

class DataStreamHandler:
    def __init__(self, port, timer_dur):
        self.port = port
        self.timer_dur = timer_dur
        self.start_test_flag = False
        self.focus_arr = np.zeros(5)  # Assuming each incoming data array has 5 elements.
        self.lock = threading.Lock()

    def start_test_process(self):
        self.start_test_flag = True
        start_time = time.time()

        def timer():
            while self.start_test_flag and (time.time() - start_time) < self.timer_dur:
                time.sleep(1)
            self.start_test_flag = False
            print("Test duration exceeded. Stopping data collection.")

        # Start the timer thread
        threading.Thread(target=timer).start()

    def handle_stream(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', self.port)
        sock.bind(server_address)

        while True:  # Run indefinitely
            received_data, address = sock.recvfrom(4096)
            if self.start_test_flag:  # Process data only if flag is True
                try:
                    json_data = json.loads(received_data)
                    with self.lock:
                        self.focus_arr += np.array(json_data["data"])
                        print(self.focus_arr)
                except json.JSONDecodeError:
                    print("Received data is not valid JSON.")

    def GetEEGData(self):
        return self.focus_arr
            

        # The socket doesn't close here, because we want to keep listening indefinitely.

# Example usage:
def StartConnection(time):
    data_handler = DataStreamHandler(port=12345, timer_dur=time)
    # Start the data collection thread immediately, it will run indefinitely
    threading.Thread(target=data_handler.handle_stream).start()
    # Use this to start the test process later, can be triggered based on specific conditions
    data_handler.start_test_process()

StartConnection(10)
