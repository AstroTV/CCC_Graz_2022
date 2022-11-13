import os
from pprint import pprint
import numpy as np
from copy import copy, deepcopy

import level1
import level2
import level3
import level4
import level5
import level6
import level7
from classes import *


def load(input_data):
    n = int(input_data[0])
    board = []
    for row in range(n):
        line = input_data[row + 1]
        out_line = []
        for x in line:
            out_line.append(x)
        board.append(out_line)

    start_row = int(input_data[n + 1].split(" ")[0]) - 1
    start_col = int(input_data[n + 1].split(" ")[1]) - 1
    max_moves = int(input_data[n + 2])

    '''
    n_moves = int(input_data[n + 2])
    moves = [*input_data[n + 3]]

    n_ghosts = int(input_data[n + 4])
    ghosts = []
    for i in range(n_ghosts):
        pos = input_data[n + 5 + i * 3]
        x = int(pos.split(" ")[0]) - 1
        y = int(pos.split(" ")[1]) - 1
        n_ghost_moves = int(input_data[n + 5 + i * 3 + 1])
        ghost_moves = [*input_data[n + 5 + i * 3 + 2]]
        ghosts.append(Ghost(x, y, n_ghost_moves, ghost_moves, 0, 0))
    original_board = deepcopy(board)
    for row in range(n):
        for col in range(n):
            if board[row][col] == "G":
                original_board[row][col] = "V"
    '''

    # return Data(n=n, board=board, pacman_row=start_row, pacman_col=start_col, n_moves=n_moves, moves=moves,
    #            n_ghosts=n_ghosts, ghosts=ghosts, original_board=original_board)

    return Data(n=n, board=board, pacman_row=start_row, pacman_col=start_col, n_moves=max_moves)


if __name__ == "__main__":
    level, quests = 4, 7
    only_one_quest = [5, 1]
    for q in range(0, quests + 1):
        if only_one_quest[1] and (q != only_one_quest[0]):
            continue
        if q == 0:
            q = "example"

        fileextension = os.getcwd() + '/level{0}/level{0}_{1}.in'.format(level, q)
        input_file = fileextension
        output_file = os.path.splitext(input_file)[0] + ".out"

        with open(input_file, 'r') as fi:
            data = load(fi.read().splitlines())
            pprint(data)

            print("=== Input {}".format(q))
            print("======================")

            if level == 1:
                result = level1.solve(data)
            elif level == 2:
                result = level2.solve(data)
            elif level == 3:
                result = level3.solve(data)
            elif level == 4:
                result = level4.solve(data)
            elif level == 5:
                result = level5.solve(data)
            elif level == 6:
                result = level6.solve(data)
            elif level == 7:
                result = level7.solve(data)

            pprint(result)

            with open(output_file, 'w+') as fo:
                fo.write(result)
