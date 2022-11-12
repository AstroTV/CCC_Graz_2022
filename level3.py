import numpy as np
from classes import *
from pprint import pprint
from copy import copy, deepcopy


def loop(data: Data):
    # Move Ghosts
    for ghost_id, ghost in enumerate(data.ghosts):
        if len(ghost.moves) > 0:
            ghost.old_col = ghost.col
            ghost.old_row = ghost.row
            if ghost.moves[0] == "L":
                ghost.col -= 1
            if ghost.moves[0] == "R":
                ghost.col += 1
            if ghost.moves[0] == "U":
                ghost.row -= 1
            if ghost.moves[0] == "D":
                ghost.row += 1

            data.board[ghost.old_row][ghost.old_col] = ghost.old_value
            # ghost.old_value = data.original_board[ghost.row][ghost.col]
            data.board[ghost.row][ghost.col] = "G"

            ghost.moves = ghost.moves[1:]
            # print("Ghost {} is in row {} col {}".format(ghost_id, ghost.row, ghost.col))

    # Move Pacman
    if data.moves and data.alive:
        data.old_col = data.pacman_col
        data.old_row = data.pacman_row
        m = data.moves[0]
        # print("Pacman moves {}".format(m))
        if m == "L":
            data.pacman_col -= 1
        if m == "R":
            data.pacman_col += 1
        if m == "U":
            data.pacman_row -= 1
        if m == "D":
            data.pacman_row += 1

        if data.board[data.pacman_row][data.pacman_col] in ["G", "W"]:
            data.alive = 0
            print("DEad at {} {}".format(data.pacman_row, data.pacman_col))
            # print_board(data)
            return

        if data.board[data.pacman_row][data.pacman_col] == "C":
            data.n_coins += 1
            print("Coins: {}, Tick: {}, at {} {}".format(data.n_coins, data.tick, data.pacman_row, data.pacman_col))

        if data.board[data.old_row][data.old_col] != "G":
            data.board[data.old_row][data.old_col] = "V"
        data.original_board[data.old_row][data.old_col] = "V"

        data.board[data.pacman_row][data.pacman_col] = "P"
        data.moves = data.moves[1:]
        # print("Pacman is in row {} col {}".format(data.pacman_row, data.pacman_col))

    for ghost in data.ghosts:
        ghost.old_value = data.original_board[ghost.row][ghost.col]


def print_board(data):
    for row in data.board:
        print("".join(row))
    print("\n")


def solve(data: Data):
    while data.tick < data.n_moves and data.alive:
        # print("Tick: {}".format(data.tick))
        loop(data)
        data.tick += 1
        # print(data.board[21][13])
    output = str(data.n_coins) + " " + ("YES" if data.alive else "NO")
    return output
