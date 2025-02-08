import random
import socket

HOST = '127.0.0.1'
PORT = 8080

WALL = "*"
NOT_WALL = " "
THIEF = "T"
TREASURE = "X"
COP = "C"

class Zira:
    def __init__(self, file_name):
        self.zone = []
        self.players = {}
        self.load_zone(file_name)
        self.load_players()

    def __str__(self):
        out = ""
        for i in range(len(self.zone)):
            out += "{:<3}".format(*[i])
            for j in range(len(self.zone[0])):
                out += str(self.zone[i][j])
            out += "\n"
        return out

    def load_zone(self, file_name):
        with open(file_name, "rb") as file:
            data = file.read()
            self.zone = [list((WALL if char else NOT_WALL) for char in data[i:i+data[0]]) for i in range(1, len(data), data[0])]

    def load_players(self):
        for player in [THIEF, TREASURE, COP]:
            row = random.randint(0, len(self.zone) - 1)
            col = random.randint(0, len(self.zone[0]) - 1)
            while self.zone[row][col] != NOT_WALL:
                row = random.randint(0, len(self.zone)-1)
                col = random.randint(0, len(self.zone[0])-1)
            self.players[player] = (row, col)
            self.zone[row][col] = player

    def player_move(self, step):
        player = self.players[THIEF]
        row_offset = 0
        col_offset = 0
        if step == "UP":
            row_offset = -1
        elif step == "DOWN":
            row_offset = 1
        elif step == "LEFT":
            col_offset = -1
        elif step == "RIGHT":
            col_offset = 1
        move = (player[0]+row_offset, player[1]+col_offset)
        if self.zone[move[0]][move[1]] == NOT_WALL:
            self.zone[move[0]][move[1]] = THIEF
            self.zone[player[0]][player[1]] = NOT_WALL
            self.players[THIEF] = move
            return "OK"
        elif self.zone[move[0]][move[1]] == TREASURE:
            return "WON"
        elif self.zone[move[0]][move[1]] == COP:
            return "LOST"
        elif self.zone[move[0]][move[1]] == WALL:
            return "WALL"

    def cop_move(self):
        player = self.players[COP]
        row_offset = random.randint(-1, 1)
        col_offset = random.randint(-1, 1)
        move = (player[0]+row_offset, player[1]+col_offset)
        if self.zone[move[0]][move[1]] == NOT_WALL:
            self.zone[move[0]][move[1]] = COP
            self.zone[player[0]][player[1]] = NOT_WALL
            self.players[COP] = move

    def get_location(self):
        return self.players[THIEF]

    def get_status(self):
        player = self.players[THIEF]
        cop = False
        treasure = False
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if self.zone[player[0]+row_offset][player[1]+col_offset] == COP:
                    cop =True
                elif self.zone[player[0]+row_offset][player[1]+col_offset] == TREASURE:
                    treasure =True
        return {"cop": cop, "treasure": treasure}

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = server.accept()
        with conn:
            print(f"Connected by {addr}")
            zira = Zira("randomwalls.bin")
            while True:
                msg = ""
                print(zira)
                data = conn.recv(1024)
                if not data:
                    break
                data = data.decode().split(" ")
                if data[0] == "MOVE":
                    result = zira.player_move(data[1])
                    zira.cop_move()
                    if result != "WON" and zira.players[COP] == zira.players[THIEF]:
                        result = "LOST"
                    msg = f"result: {result}"
                elif data[0] == "STATUS":
                    near_dict = zira.get_status()
                    if near_dict["cop"]:
                        msg = "status: COP NEAR"
                    elif near_dict["treasure"]:
                        msg = "status: TREASURE NEAR"
                    else:
                        msg = "status: GAME ON"
                    zira.cop_move()
                elif data[0] == "LOCATION":
                    location = zira.get_location()
                    msg = f"location: {location[0]},{location[1]}"
                    zira.cop_move()
                conn.sendall(msg.encode())

if __name__ == "__main__":
    main()