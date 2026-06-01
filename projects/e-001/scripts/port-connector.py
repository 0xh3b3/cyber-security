import socket

def main():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port to connect to
    host = 'localhost'  # Change this to the target host
    for i in range(0, 65535):
        try:
            # Connect to the server
            s.settimeout(5)
            s.connect((host, int(i)))
            print(f"Connected to {host}:{int(i)}")

            # Receive a response from the server
            response = s.recv(1024).decode()
            print(f"port {i} is open")

        except socket.timeout:
            print(f"Port {i} is closed or filtered")
        finally:
            # Close the connection
            s.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()