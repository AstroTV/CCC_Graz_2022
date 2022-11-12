import numpy as np
from classes import *


def solve(data: Data):
    pacman_row = data.pacman_row
    pacman_col = data.pacman_col

    n_coins = 0
    for i, m in enumerate(data.moves):
        if i > 153:
            break

        # print("Pacman on row {} col {} -> {}".format(pacman_row, pacman_col, data.board[pacman_row][pacman_col]))
        if m == "L":
            pacman_col -= 1
        if m == "R":
            pacman_col += 1
        if m == "U":
            pacman_row -= 1
        if m == "D":
            pacman_row += 1
        if data.board[pacman_row][pacman_col] == "C":
            data.board[pacman_row][pacman_col] = "V"
            n_coins += 1
            print("Coins: {}, Tick: {}, at {} {}".format(n_coins, i, pacman_row, pacman_col))
    output = str(n_coins)
    return output
