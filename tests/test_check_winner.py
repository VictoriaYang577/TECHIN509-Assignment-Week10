import pytest
from models.board import Board

def test_row_winner():
    board = Board()
    board.grid = [["X", "X", "X"], [" ", "O", " "], ["O", " ", "O"]]
    assert board.check_winner() == "X"

def test_column_winner():
    board = Board()
    board.grid = [["X", "O", " "], ["X", "O", " "], [" ", "O", " "]]
    assert board.check_winner() == "O"

def test_diagonal_winner():
    board = Board()
    board.grid = [["X", " ", "O"], [" ", "X", " "], ["O", " ", "X"]]
    assert board.check_winner() == "X"

def test_no_winner():
    board = Board()
    board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert board.check_winner() == ""

def test_empty_board():
    board = Board()
    board.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    assert board.check_winner() == ""
