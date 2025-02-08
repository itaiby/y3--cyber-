import socket

HOST = '127.0.0.1'
PORT = 8080

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        data = ""
        while data not in ["result: WON", "result: LOST"]:
            msg = ""
            command = input("Enter a command (move/status/location): ")
            if command == "move":
                direction = ""
                while direction not in ["up", "down", "left", "right"]:
                    direction = input("Enter direction (up/down/left/right): ")
                    if direction not in ["up", "down", "left", "right"]:
                        print("Direction invalid, try again.")
                msg = f"MOVE {direction.upper()}"
            elif command == "status":
                msg = "STATUS"
            elif command == "location":
                msg = "LOCATION"
            else:
                print("Command invalid, try again.")
                continue
            client.sendall(msg.encode())
            data = client.recv(1024).decode()
            print(data)

if __name__ == "__main__":
    main()