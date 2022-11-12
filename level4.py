import numpy as np
from classes import *
from copy import copy, deepcopy
from pprint import pprint

from math import inf
from collections import deque

inv_move = {"U": "D", "D": "U", "R": "L", "L": "R"}


def solve(data: Data):
    moves = []
    coins = sum([sum([c == "C" for c in row]) for row in data.board])

    data.board[data.pacman_row][data.pacman_col] = "C"

    while coins > 0:
        print(moves)
        pprint(data.board)
        if data.board[data.pacman_row][data.pacman_col - 1] == "C":
            moves.append("L")
            data.board[data.pacman_row][data.pacman_col - 1] = "V"
            data.pacman_col -= 1
            coins -= 1
            continue
        elif data.board[data.pacman_row - 1][data.pacman_col] == "C":
            moves.append("U")
            data.board[data.pacman_row - 1][data.pacman_col] = "V"
            data.pacman_row -= 1
            coins -= 1
            continue
        elif data.board[data.pacman_row][data.pacman_col + 1] == "C":
            moves.append("R")
            data.board[data.pacman_row][data.pacman_col + 1] = "V"
            data.pacman_col += 1
            coins -= 1
            continue
        elif data.board[data.pacman_row + 1][data.pacman_col] == "C":
            moves.append("D")
            data.board[data.pacman_row + 1][data.pacman_col] = "V"
            data.pacman_row += 1
            coins -= 1
            continue
        else:
            # Go back until we have a coin
            reverse_steps = []
            reverse_index = 1
            while True:
                print("Going back, reverse_index: {}".format(reverse_index))
                print(moves[-reverse_index])
                if moves[-reverse_index] == inv_move["L"]:
                    data.pacman_col -= 1
                if moves[-reverse_index] == inv_move["U"]:
                    data.pacman_row -= 1
                if moves[-reverse_index] == inv_move["R"]:
                    data.pacman_col += 1
                if moves[-reverse_index] == inv_move["D"]:
                    data.pacman_row += 1

                reverse_steps.append(inv_move[moves[-reverse_index]])
                reverse_index += 1

                if data.board[data.pacman_row][data.pacman_col - 1] == "C":
                    break
                elif data.board[data.pacman_row - 1][data.pacman_col] == "C":
                    break
                elif data.board[data.pacman_row][data.pacman_col + 1] == "C":
                    break
                elif data.board[data.pacman_row + 1][data.pacman_col] == "C":
                    break
            moves += reverse_steps

    output = "".join(moves)
    return output
