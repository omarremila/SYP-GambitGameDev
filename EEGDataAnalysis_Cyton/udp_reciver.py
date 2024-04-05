import socket
import threading
import datetime
import os

# Function to handle incoming UDP data for a particular stream
def handle_stream(port, file_name):
    # Determine the folder based on the file name
    if 'TimeSeries' in file_name:
        folder = 'TimeSeriesData'
    elif 'BandPower' in file_name:
        folder = 'BandPassData'
    elif 'FFT' in file_name:
        folder = 'FFTData'
    else:
        folder = 'OtherData'  # Default case, if needed

    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Generate a datetime string
    datetime_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Modify the file name to include the datetime
    modified_file_name = f"{folder}/{datetime_str}_{file_name}"

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the loopback address and port
    server_address = ('127.0.0.1', port)
    sock.bind(server_address)

    # Open a file to save the data
    with open(modified_file_name, 'wb') as file:
        print(f"Listening for data on port {port}...")
        # Listen for incoming data
        while True:
            data, address = sock.recvfrom(4096)
            print(f"Received {len(data)} bytes from {address}")
            # Write the data to a file
            file.write(data)
            # Here you might want to add a newline or other delimiter depending on your data format

# Creating threads for each stream
stream1_thread = threading.Thread(target=handle_stream, args=(12345, 'TimeSeries.json'))
stream2_thread = threading.Thread(target=handle_stream, args=(12346, 'BandPower.json'))
stream3_thread = threading.Thread(target=handle_stream, args=(12347, 'FFT.bin'))

# Starting the threads
stream1_thread.start()
stream2_thread.start()
stream3_thread.start()
