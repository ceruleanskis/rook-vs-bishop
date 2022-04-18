from colorama import init
from enum import Enum
from random import randint

from rook_vs_bishop.board import Board, Bishop, Position, Rook
from rook_vs_bishop.constants import CoinTossResult, Direction
from rook_vs_bishop.game_utils import GameUtils

# init colorama for colors/readability of output
init()


class Game:
    ''' A class to handle the core gameplay logic '''

    def __init__(self, board: Board, total_rounds: int = 15):
        self.board = board
        self.log = []
        self.total_rounds = total_rounds
        self.current_round = 1
        self.bishop_path = GameUtils.get_diagonals_from_indices(
            self.board.bishop.position.get_tuple_representation()
        )

    @staticmethod
    def coin_toss() -> CoinTossResult:
        return CoinTossResult(randint(0, 1))

    @staticmethod
    def d6_roll() -> int:
        return randint(1, 6)

    def print_current_status(self, show_path=False):
        ''' Log the board, along with pieces and their positions. '''

        self.board.render(show_path)
        rook_current_pos = self.board.rook.position.get_notation()
        bishop_current_pos = self.board.bishop.position.get_notation()

        print(f'\nRook: {rook_current_pos}')
        print(f'Bishop: {bishop_current_pos}')

    def coin_toss_step(self) -> Direction:
        '''
        Flips a coin, and the outcome determines whether to move the 
        rook up or right.

        :return: a Direction indicating which way to move the rook
        :rtype: Direction
        '''

        coin_toss = Game.coin_toss()
        direction = Direction.UP if coin_toss == CoinTossResult.HEADS \
            else Direction.RIGHT

        print(f'A coin is flipped. The result is {coin_toss.name}.')
        return direction

    def dice_roll_step(self) -> int:
        ''' Rolls 2d6 and returns the sum '''

        roll_2d6_result = [Game.d6_roll(), Game.d6_roll()]
        roll_2d6_sum = sum(roll_2d6_result)
        print(f'Two d6 are rolled. The result is '
              f'{roll_2d6_result} = {roll_2d6_sum}.')
        return roll_2d6_sum

    def move_rook_step(self, direction: Direction, amount: int):
        '''
        Moves the rook in the given direction by the given amount of 
        squares.

        :param direction: The direction to move the rook
        :type direction: Direction
        :param amount: The number of squares to move
        :type amount: int
        '''

        rook_current_pos = self.board.rook.position.get_notation()
        self.board.rook.move(
            direction=direction,
            amount=amount
        )
        rook_new_pos = self.board.rook.position.get_notation()
        print(f'Rook moves {amount} squares '
              f'{direction.name}, from {rook_current_pos} to {rook_new_pos}.\n')

    def bishop_can_capture_rook(self) -> bool:
        ''' 
        Determine if the rook's current position is a square 
        that the bishop can move to. 
        '''
        rook_pos = self.board.rook.position.get_tuple_representation()
        return rook_pos in self.bishop_path

    def rook_can_capture_bishop(self) -> bool:
        '''
        Determine if rook is on the same row or col as bishop.
        If so, the rook can capture the bishop.
        '''
        rook_pos = self.board.rook.position
        bishop_pos = self.board.bishop.position
        return rook_pos.rank == bishop_pos.rank or\
             rook_pos.file == bishop_pos.file

    def play(self):
        '''
        The main game loop. 
        The rook moves until it is captured, it captures the bishop,
        or the total amount of rounds are exceeded.
        '''
        winner = 'Rook'
        print('Game Start\n')
        self.print_current_status()

        while self.current_round <= self.total_rounds:
            print('\n============================================\n')
            print(f'Round {self.current_round}\n')

            direction = self.coin_toss_step()
            roll_2d6_sum = self.dice_roll_step()
            self.move_rook_step(direction, amount=roll_2d6_sum)

            if self.bishop_can_capture_rook():
                self.print_current_status(show_path=True)
                print('\nBishop captures rook.')
                winner = 'Bishop'
                break
            
            self.print_current_status()

            self.current_round += 1

        if winner == 'Rook':
            print(f'\nRook survived {self.total_rounds} rounds.')
        print(f'{winner} wins!')
