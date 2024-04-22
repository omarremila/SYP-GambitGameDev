import socket
import threading
import datetime
import os
import time  # Import time module for tracking intervals

def handle_stream(port, file_name):
    """
    Handles incoming UDP data streams by collecting data for 10 seconds and writing it to a file.

    :param port: int - The port number to listen on.
    :param file_name: str - The base name of the file to write incoming data to.
    """
    # Determine the appropriate folder based on the type of data in file_name
    if 'TimeSeries' in file_name:
        folder = 'TimeSeriesData'
    elif 'BandPower' in file_name:
        folder = 'BandPassData'
    elif 'FFT' in file_name:
        folder = 'FFTData'
    else:
        folder = 'OtherData'  # Default folder for unspecified data types

    # Create the folder if it does not already exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Generate a timestamp for file naming to avoid overwriting previous files
    datetime_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    modified_file_name = f"{folder}/{datetime_str}_{file_name}"

    # Setup the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', port)
    sock.bind(server_address)

    # Start collecting data
    start_time = time.time()
    with open(modified_file_name, 'wb') as file:
        print(f"Listening for data on port {port} for 10 seconds...")
        while True:
            # Stop collecting data after 10 seconds
            if time.time() - start_time > 10:
                print("10 seconds have passed. Stopping data collection.")
                break

            # Set socket timeout to prevent indefinite blocking
            sock.settimeout(1)
            try:
                data, address = sock.recvfrom(4096)
                print(f"Received {len(data)} bytes from {address}")
                file.write(data)
                file.flush()  # Flush the data to disk after writing
            except socket.timeout:
                # Handle case where no data is received within the timeout period
                continue

    # Cleanup by closing the socket
    sock.close()

# Run the function in a script-safe block to prevent accidental execution when imported
if __name__ == "__main__":
    # Setup and start threads for multiple data streams
    threads = [
        threading.Thread(target=handle_stream, args=(12345, 'TimeSeries.json')),
        threading.Thread(target=handle_stream, args=(12346, 'BandPower.json')),
        threading.Thread(target=handle_stream, args=(12347, 'FFT.bin'))
    ]

    for thread in threads:
        thread.start()
