import Morse
import socket

def start_server():
    host = '127.0.0.1'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    continue
                data = data.decode()
                encryption, data = data[:data.index(" ")], data[data.index(" ")+1:]
                if encryption.lower() in "caeser":
                    alphabet = "abcdefghijklmnopqrstuvwxyz"
                    decoded_text = ""
                    key, data = int(data[:data.index(" ")]), data[data.index(" ")+1:]
                    for char in data.lower():
                        if char.isalpha():
                            decoded_text += alphabet[(alphabet.index(char) - key) % 26]
                        else:
                            decoded_text += char
                    data = decoded_text
                elif encryption.lower() in "morse":
                    data = Morse.translate_morse(data)
                conn.sendall(data.encode())

if __name__ == "__main__":
    start_server()
