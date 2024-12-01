import socket
from argparse import ArgumentError
from multiprocessing.managers import Value


def start_client():
    host = '127.0.0.1'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            try:
                file_path = input("Enter morse file name: ")
                encryption = input("Enter type of encryption: ")
                data = b""
                with open(file_path, 'r') as file:
                    if encryption.lower() in ["morse","caeser"]:
                        data += (encryption.lower()+" ").encode()
                    else:
                        print("Unvalid encryption type.")
                        continue
                    data += (file.read().strip("\n")).encode()
                    client_socket.sendall(data)
                data = client_socket.recv(1024)
                print(f"Received from server: {data.decode()}")
            except Exception as e:
                print(f"Error raised: {e}")


if __name__ == "__main__":
    start_client()
