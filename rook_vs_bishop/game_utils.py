from typing import Tuple
import re

from rook_vs_bishop.constants import BOARD_SIZE

class GameUtils:
    ''' Useful helper methods for game functionality '''

    @staticmethod
    def get_index_from_file(file: str) -> int:
        ''' Given a file a-h, returns its int index. '''

        # matches a str containing only a single letter from a to h
        match_expression = r'^[A-Ha-h]{1}$'

        if re.match(match_expression, file):
            # returns 0 for a, 1 for b, ... 7 for h
            return ord(file) - ord('a')
        else:
            raise ValueError(
                'File must be a string containing only a single letter from a to h')

    @staticmethod
    def get_index_from_rank(rank: str) -> int:
        return BOARD_SIZE - int(rank)

    @staticmethod
    def get_indices_from_notation(notation: str) -> Tuple:
        ''' Converts str notation to numeric tuple '''
        notation_list = list(notation)
        file_index = GameUtils.get_index_from_file(notation_list[0])
        rank_index = GameUtils.get_index_from_rank(notation_list[1])

        return (rank_index, file_index)

    @staticmethod
    def get_notation_from_indices(indices: Tuple) -> str:
        ''' Converts numeric tuple to str notation '''
        rank = indices[0]
        file = indices[1]

        str_rank = str(8 - rank)
        chr_file = chr(ord('a') + file)

        return f'{chr_file}{str_rank}'

    @staticmethod
    def get_diagonals_from_indices(indices: Tuple):
        ''' Calculates the diagonal positions from a given position '''

        # TODO: generalize & refactor this function per DRY

        diagonals = []

        # get top right
        i = indices[0] + 1
        j = indices[1] - 1

        while i <= BOARD_SIZE - 1 and j >= 0:
            diagonals.append((i, j))
            i += 1
            j -= 1

        # get bottom right
        i = indices[0] + 1
        j = indices[1] + 1

        while i <= BOARD_SIZE - 1 and j <= BOARD_SIZE - 1:
            diagonals.append((i, j))
            i += 1
            j += 1

        # get bottom left
        i = indices[0] - 1
        j = indices[1] + 1

        while i >= 0 and j <= BOARD_SIZE - 1:
            diagonals.append((i, j))
            i -= 1
            j += 1

        # get top left
        i = indices[0] - 1
        j = indices[1] - 1

        while i >= 0 and j >= 0:
            diagonals.append((i, j))
            i -= 1
            j -= 1

        return diagonals
