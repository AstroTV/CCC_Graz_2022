from dataclasses import dataclass


# from collections import namedtuple


# Task = namedtuple('Task', ['id', 'powerdemand','startint', 'endint'])

@dataclass
class Ghost:
    row: int
    col: int
    n_moves: int
    moves: [str]
    old_row: int
    old_col: int
    old_value: str = "V"


@dataclass
class Data:
    n: int
    board: [[str]]
    pacman_row: int
    pacman_col: int
    n_moves: int
    '''
    moves: [str]
    n_ghosts: int
    ghosts: [Ghost]
    original_board: [[str]]
    n_coins: int = 0
    alive = 1

    tick: int = 0
    old_row: int = 0
    old_col: int = 0
    '''


@dataclass
class Point:
    row: int
    col: int
    visited: bool = False

