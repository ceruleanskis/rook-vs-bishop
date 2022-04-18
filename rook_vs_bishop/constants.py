''' Constants for use in game functions '''

from enum import Enum

BOARD_SIZE = 8  # the length of a side of the (square) board


class CoinTossResult(Enum):
    ''' An enum representing a coin toss outcome '''

    HEADS = 0
    TAILS = 1


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    TOP_RIGHT = (-1, 1)
    TOP_LEFT = (-1, -1)
    BOTTOM_RIGHT = (1, 1)
    BOTTOM_LEFT = (1, -1)
