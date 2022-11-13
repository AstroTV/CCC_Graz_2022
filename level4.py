import math
from classes import *


def print_pac(data):
    for row in range(data.n):
        pretty_row = ""
        for col in range(data.n):
            if data.board[row][col] in ['W', 'G']:
                pretty_row += "█"
            elif data.pacman_row == row and data.pacman_col == col:
                pretty_row += "@"
            else:
                pretty_row += data.board[row][col]
        print(pretty_row)
    print("\n")


def get_numeric_neighbors(row, col, lab):
    neighbors = []
    if row > 0 and lab[row - 1][col].isnumeric():
        neighbors.append(int(lab[row - 1][col]))
    if col > 0 and lab[row][col - 1].isnumeric():
        neighbors.append(int(lab[row][col - 1]))
    if row < len(lab) - 1 and lab[row + 1][col].isnumeric():
        neighbors.append(int(lab[row + 1][col]))
    if col < len(lab) - 1 and lab[row][col + 1].isnumeric():
        neighbors.append(int(lab[row][col + 1]))
    return sorted(neighbors)


# We calculate the path from the coin to pacman, so we have to reverse it
def reverse_path(path):
    inv = {"U": "D", "D": "U", "L": "R", "R": "L"}
    path = path[::-1]
    for i in range(len(path)):
        path[i] = inv[path[i]]
    return path


def get_step_towards_pacman(row, col, lab):
    up = math.inf
    left = math.inf
    down = math.inf
    right = math.inf
    if row > 0 and lab[row - 1][col].isnumeric():
        up = int(lab[row - 1][col])
    if col > 0 and lab[row][col - 1].isnumeric():
        left = int(lab[row][col - 1])
    if row < len(lab) - 1 and lab[row + 1][col].isnumeric():
        down = int(lab[row + 1][col])
    if col < len(lab) - 1 and lab[row][col + 1].isnumeric():
        right = int(lab[row][col + 1])

    if up == min([up, left, down, right]):
        return "U", row - 1, col
    if left == min([up, left, down, right]):
        return "L", row, col - 1
    if down == min([up, left, down, right]):
        return "D", row + 1, col
    if right == min([up, left, down, right]):
        return "R", row, col + 1


def shortest_path_to_coin(data):
    # Create a new labyrinth where Pacman starts with 0
    # We use the A* algorith to find the nearest coin from pacmans location
    lab = []
    for row in range(data.n):
        line = []
        for col in range(data.n):
            if row == data.pacman_row and col == data.pacman_col:
                line.append("0")
            elif data.board[row][col] == "C":
                line.append("C")
            elif data.board[row][col] in ["W", "G"]:
                line.append("█")
            else:
                line.append(" ")
        lab.append(line)

    # A* implementation
    found = False
    r = 0
    c = 0
    while not found:
        for row in range(data.n):
            for col in range(data.n):
                if lab[row][col] == " ":
                    neighbors = get_numeric_neighbors(row, col, lab)
                    if neighbors:
                        lab[row][col] = str(neighbors[0] + 1)
                if lab[row][col] == "C":
                    neighbors = get_numeric_neighbors(row, col, lab)
                    if neighbors:
                        found = True
                        r = row
                        c = col
                        break
            if found:
                break

    # Now we have to follow the path step by step from the coin to pacman
    coin_row = r
    coin_col = c
    path = []
    while lab[r][c] != "0":
        step, r, c = get_step_towards_pacman(r, c, lab)
        path.append(step)

    # We return the reversed path from the coin to pacman together with his new position
    return reverse_path(path), coin_row, coin_col


def solve(data: Data):
    moves = []
    coins = sum([sum([c == "C" for c in row]) for row in data.board])

    print_pac(data)
    # We calculate a path to a coin until there are no more coins on the board
    while coins > 0:
        path, new_row, new_col = shortest_path_to_coin(data)
        print("Path: {}".format(path))
        # Append the moves that pacman made
        moves += path
        # Update the board after the coin is gone and pacman has his new position
        data.board[data.pacman_row][data.pacman_col] = " "
        data.board[new_row][new_col] = "P"
        data.pacman_row = new_row
        data.pacman_col = new_col
        coins -= 1
        print_pac(data)
        
    print(len(moves))
    output = "".join(moves)
    return output
