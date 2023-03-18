from Starters import *

if __name__ == "__main__":
    """Testing Starter Files and Board"""
    board = Board()
    board.readFile("../sudoku-solver-py/board.txt")

    print(board)
