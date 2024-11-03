def factorial_calculate(num):
    if num == 1:
        return 1
    return multiplication_calculate(factorial_calculate(num-1),num)

def multiplication_calculate(num1, num2):
    if num2 == 1:
        return num1
    return addition_calculate(multiplication_calculate(num1,num2-1), num1)

def addition_calculate(num1, num2):
    if num2 == 0:
        return num1
    return addition_calculate(num1,num2-1) + 1

def maze_solve(file_path=""):
    with open(file_path, "r") as file:
        array = [row.split(",") for row in file.read().splitlines()]
        return maze_array_solve(array)

def maze_array_solve(array, row=0, col=0, direction=1):

    if row == len(array)-1 and col == len(array[0])-1:
        for line in array:
            print(line)
        return True
    if row == 0 and col == 0 and (direction == 2 or direction == 3):
        return False
    return maze_array_solve(array, *next_move(array, row, col, direction))

def next_move(array, row, col, direction):
    directions = {0: (row-1, col, 0),1: (row, col+1, 1), 2: (row+1, col, 2), 3: (row, col-1, 3)}
    array[row][col] = "■"
    for i in [1,0,3,2]:
        try_row, try_col, try_direction = directions[(direction+i)%4]
        if try_row < 0 or try_col < 0 or try_row > len(array)-1 or try_col > len(array[0])-1:
            continue
        if array[try_row][try_col] in ["1","■"]:
            if array[try_row][try_col] == "■":
                array[row][col] = "1"
            else:
                array[try_row][try_col] = "■"
            return try_row, try_col, try_direction





print(maze_solve("maze.txt"))