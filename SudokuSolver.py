from Starters import *


class SudokuSolver:

    def __init__(self, board) -> None:
        self.board = board

    def findNextCell(self):
        """Find the next cell to be checked"""

        pass

    def findNextValue(self, cell: Cell):
        """Find the next value for the cell"""

        for i in range(cell.getValue(), 10):
            if board.validValue(cell.getRow(), cell.getCol(), i):
                cell.setValue(i)
                return i

        cell.setValue(0)
        return 0

    def solve(self):
        """Solve the board using backtracking, stacks and DFS"""

        pass

    def solveRecursive(self):
        """Solve the board attribute recursively"""

        pass

    def getBoard(self):
        """Get the board being solved"""

        return self.board


if __name__ == "__main__":
    board = Board()
    sudokuSolver = SudokuSolver(board)

    sudokuSolver.solve()
    print(sudokuSolver.getBoard())
