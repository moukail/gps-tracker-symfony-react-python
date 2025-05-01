import bluetooth
import serial

# Bluetooth server settings
server_address = ""  # Leave empty to bind to any Bluetooth adapter
server_port = bluetooth.PORT_ANY  # Use any available port

# USB settings
usb_port = '/dev/ttyUSB0'  # Adjust based on your USB device (e.g., COM3 for Windows, /dev/ttyUSB0 for Linux)
baud_rate = 9600  # Baud rate for the USB device

def start_bluetooth_server():
    # Create a Bluetooth socket
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Bind the socket to the server address and port
    server_sock.bind((server_address, server_port))

    # Listen for incoming connections (1 means only one connection at a time)
    server_sock.listen(1)

    # Get the port assigned for the connection
    port = server_sock.getsockname()[1]
    print(f"Bluetooth server started on port {port}")

    return server_sock

def handle_client(client_sock, usb_serial):
    try:
        while True:
            # Receive data from the Bluetooth client
            data = client_sock.recv(1024)
            if not data:
                break  # Client has disconnected

            print(f"Received from Bluetooth: {data}")

            # Forward the received data to the USB device
            usb_serial.write(data)
            print(f"Forwarded to USB: {data}")

    except bluetooth.BluetoothError as e:
        print(f"Bluetooth error: {e}")

    finally:
        # Close the client connection
        client_sock.close()

def main():
    # Start the Bluetooth server
    server_sock = start_bluetooth_server()

    # Open the USB port for communication
    usb_serial = serial.Serial(usb_port, baud_rate)

    try:
        while True:
            # Wait for a Bluetooth client to connect
            print("Waiting for Bluetooth client to connect...")
            client_sock, client_address = server_sock.accept()
            print(f"Accepted connection from {client_address}")

            # Handle the Bluetooth client and forward data to USB
            handle_client(client_sock, usb_serial)

    except KeyboardInterrupt:
        print("Server shutting down.")

    finally:
        # Close the server and USB connections
        server_sock.close()
        usb_serial.close()

if __name__ == "__main__":
    main()