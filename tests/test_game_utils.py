import pytest

from rook_vs_bishop.game_utils import GameUtils


def test_get_index_from_file_valid():
    assert GameUtils.get_index_from_file('a') == 0
    assert GameUtils.get_index_from_file('b') == 1
    assert GameUtils.get_index_from_file('c') == 2
    assert GameUtils.get_index_from_file('d') == 3
    assert GameUtils.get_index_from_file('e') == 4
    assert GameUtils.get_index_from_file('f') == 5
    assert GameUtils.get_index_from_file('g') == 6
    assert GameUtils.get_index_from_file('h') == 7


def test_get_index_from_file_invalid():
    with pytest.raises(Exception) as excinfo:
        GameUtils.get_index_from_file('')
    assert str(excinfo.typename) == 'ValueError'

    with pytest.raises(Exception) as excinfo:
        GameUtils.get_index_from_file('  ')
    assert str(excinfo.typename) == 'ValueError'

    with pytest.raises(Exception) as excinfo:
        GameUtils.get_index_from_file('ag')
    assert str(excinfo.typename) == 'ValueError'

    with pytest.raises(Exception) as excinfo:
        GameUtils.get_index_from_file('j12')
    assert str(excinfo.typename) == 'ValueError'

    with pytest.raises(Exception) as excinfo:
        GameUtils.get_index_from_file(4)
    assert str(excinfo.typename) == 'TypeError'


def test_get_index_from_rank_valid():
    assert GameUtils.get_index_from_rank(1) == 7
    assert GameUtils.get_index_from_rank(2) == 6
    assert GameUtils.get_index_from_rank(3) == 5
    assert GameUtils.get_index_from_rank(4) == 4
    assert GameUtils.get_index_from_rank(5) == 3
    assert GameUtils.get_index_from_rank(6) == 2
    assert GameUtils.get_index_from_rank(7) == 1
    assert GameUtils.get_index_from_rank(8) == 0


def test_get_indices_from_notation():
    assert GameUtils.get_indices_from_notation('h1') == (7, 7)
    assert GameUtils.get_indices_from_notation('c3') == (5, 2)
    assert GameUtils.get_indices_from_notation('a8') == (0, 0)
    assert GameUtils.get_indices_from_notation('a1') == (7, 0)
    assert GameUtils.get_indices_from_notation('h8') == (0, 7)


def test_get_diagonals_from_indices():
    pos = (2, 5)

    expected = [
        # top right
        (3, 4),
        (4, 3),
        (5, 2),
        (6, 1),
        (7, 0),

        # bottom right
        (3, 6),
        (4, 7),

        # bottom left
        (1, 6),
        (0, 7),

        # top left
        (1, 4),
        (0, 3)
    ]
    expected.sort(key=lambda x: x[0])

    actual = GameUtils.get_diagonals_from_indices(pos)
    actual.sort(key=lambda x: x[0])

    assert actual == expected
