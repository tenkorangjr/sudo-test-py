from Starters import *
import time


class SudokuSolver:

    def __init__(self, board: Board) -> None:
        self.board = board

    def solveAllSolutions(self) -> list:
        """Get a list of all the solutions"""

        stack = []
        output = []

        while (len(stack) < self.board.unspecifiedCells):

            next = self.findNextCell()

            while (not next and len(stack) > 0):
                temp: Cell = stack.pop()
                tempVal = self.findNextValue(temp)
                temp.setValue(tempVal)
                if tempVal != 0:
                    next = temp

            if (not next):
                return False
            else:
                stack.append(next)
                time.sleep(0.3)

                if len(stack) == self.board.unspecifiedCells:
                    output.append(stack[:])
                    last: Cell = stack.pop()
                    last.setValue(0)
                    next: Cell = stack.pop()
                    nextVal = self.findNextValue(next)
                    next.setValue(nextVal)
                    while (nextVal == 0):
                        next = stack.pop()
                        nextVal = self.findNextValue(next)
                        next.setValue(nextVal)

                    if (len(stack) == 1):
                        temp = stack.pop()
                        tempVal = self.findNextValue(temp)
                        temp.setValue(tempVal)

                        if not tempVal:  # tempVal is zero
                            return True

        return True

    def findNextCell(self) -> Cell:
        """Find the next cell to be checked and modified"""

        for row in range(0, 9):
            for col in range(0, 9):
                if int(self.board.getCell(row, col).getValue()) == 0:
                    new_val = self.findNextValue(self.board.getCell(row, col))
                    self.board.getCell(row, col).setValue(new_val)
                    if new_val != 0:
                        return self.board.getCell(row, col)
                    else:
                        return None

        return None

    def findNextValue(self, cell: Cell) -> int:
        """Find the next value for the cell"""

        for i in range(cell.getValue() + 1, 10):
            if self.board.validValue(cell.getRow(), cell.getCol(), i):
                return i

        return 0

    def solve(self) -> bool:
        """Solve the board using backtracking, stacks and DFS"""

        stack = Stack()

        while stack.size() < self.board.unspecifiedCells:

            next: Cell = self.findNextCell()
            while not next and stack.size() > 0:  # need to backtrack

                temp_cell: Cell = stack.pop()
                temp_value = self.findNextValue(temp_cell)
                temp_cell.setValue(temp_value)

                if temp_value != 0:
                    next = temp_cell

            if next == None:
                return False
            else:
                stack.push(next)

        return True

    def getBoard(self) -> Board:
        """Get the board being solved"""

        return self.board


if __name__ == "__main__":
    board = Board()
    board.readFile("board.txt")
    print(board)
    solver = SudokuSolver(board)
    solver.solveAllSolutions()
    print(board)
