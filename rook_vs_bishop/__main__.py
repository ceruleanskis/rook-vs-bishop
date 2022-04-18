from rook_vs_bishop.board import Board, Bishop, Position, Rook
from rook_vs_bishop.game import Game
from rook_vs_bishop.game_utils import GameUtils


def main() -> None:
    rook_starting_pos = Position(
        GameUtils.get_indices_from_notation('h1')
    )
    rook = Rook(position=rook_starting_pos)

    bishop_starting_pos = Position(
        GameUtils.get_indices_from_notation('c3')
    )
    bishop = Bishop(position=bishop_starting_pos)

    board = Board(rook=rook, bishop=bishop)
    game = Game(board=board)

    game.play()


if __name__ == '__main__':
    main()
