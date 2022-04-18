""" A class representing a chess board and its state """

from copy import deepcopy
from typing import List, Tuple

from colorama import Fore, Back, Style

from rook_vs_bishop.constants import BOARD_SIZE, Color, Direction
from rook_vs_bishop.game_utils import GameUtils


class Position:
    ''' An object that contains the rank and file state on the board '''
    def __init__(self, indices: Tuple):
        self.rank = indices[0]
        self.file = indices[1]

    def get_notation(self):
        return GameUtils.get_notation_from_indices(
            (self.rank, self.file)
        )

    def get_tuple_representation(self):
        return (self.rank, self.file)

    def __str__(self):
        return str((self.rank, self.file))

    def __eq__(self, o):
        return o.rank == self.rank and o.file == self.file


class Piece:
    ''' A generic class for the types of pieces on the board '''
    def __init__(self, position: Position, char: str, color: Color):
        self.position = position
        self.char = char

    def move(self, direction: Direction, amount: int) -> Position:
        raise NotImplementedError

    def __str__(self):
        return self.char


class Bishop(Piece):
    def __init__(self, position: Position):
        super().__init__(position, char='B', color=Color.WHITE)


class Rook(Piece):
    def __init__(self, position: Position):
        super().__init__(position, char='R', color=Color.BLACK)

    def move(self, direction: Direction, amount: int) -> Position:
        ''' Moves the rook in the direction by the amount. '''
        valid_directions = [
            Direction.UP,
            Direction.DOWN,
            Direction.LEFT,
            Direction.RIGHT
        ]
        if direction not in valid_directions:
            raise ValueError('Rook can only move horizontally and vertically.')

        direction_val = direction.value
        vector = (direction_val[0] * amount, direction_val[1] * amount)

        new_rank = (vector[0] + self.position.rank) % BOARD_SIZE
        new_file = (vector[1] + self.position.file) % BOARD_SIZE
        self.position = Position((new_rank, new_file))


class Square:
    ''' A tile on the board '''
    def __init__(self, position: Position):
        self.position = position

    @property
    def color(self) -> Color:
        if self.position.file % 2 != self.position.rank % 2:
            return Color.BLACK
        else:
            return Color.WHITE

    def __str__(self):
        return ' '


class Board:
    ''' An object containing pieces and squares '''
    def __init__(self, rook: Rook, bishop: Bishop):
        self.rook = rook
        self.bishop = bishop
        self.squares = [[Square(Position((i, j))) for j in range(BOARD_SIZE)]
                        for i in range(BOARD_SIZE)]
        self.diagonals = GameUtils.get_diagonals_from_indices(
            (self.bishop.position.rank, self.bishop.position.file)
        )

    def get_style_prefix_for_render(self, current_sq, show_path=False):
        ''' Decides which color to render based on square contents '''
        style_prefix = ''

        if type(current_sq) == Rook:
            style_prefix += f'{Fore.RED}{Style.BRIGHT}'

        elif type(current_sq) == Bishop:
            style_prefix += f'{Fore.GREEN}{Style.BRIGHT}'
    
        elif show_path and current_sq.position.get_tuple_representation() in self.diagonals:
            style_prefix = Back.RED

        else:
            style_prefix = Back.BLACK if current_sq.color == Color.BLACK else Back.WHITE

        return style_prefix

    def render(self, show_path=False):
        ''' Prints a visual representation of the board '''
        
        result = ''
        print_square = deepcopy(self.squares)

        for piece in [self.rook, self.bishop]:
            print_square[piece.position.rank][piece.position.file] = piece

        for i in range(BOARD_SIZE):
            line_to_print = str(BOARD_SIZE-i)

            for j in range(BOARD_SIZE):
                current = print_square[i][j]
                style_prefix = self.get_style_prefix_for_render(
                    current, show_path)
                line_to_print += f' {style_prefix}{str(current)}{Style.RESET_ALL}'

            result += f'{line_to_print}\n'

        rank_markers = '  ' + \
            ' '.join([chr(ord('a') + i) for i in range(BOARD_SIZE)])
        result += rank_markers

        print(result)
