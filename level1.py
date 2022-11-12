import numpy as np
from classes import *


def solve(data: Data):
    n_coins = 0
    for row in data.board:
        for col in row:
            if col == "C":
                n_coins += 1
    output = str(n_coins)
    return output
