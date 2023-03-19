class Cell:

    def __init__(self, row=-1, col=-1, value=0, is_locked=False) -> None:
        self.row: int = row
        self.col: int = col
        self.value: int = value
        self.is_locked: bool = is_locked

    def __str__(self) -> str:
        """String Representation of Cell"""

        return str(self.value)

    def getRow(self) -> int:
        """Get the Row of Cell"""

        return self.row

    def getCol(self) -> int:
        """Get the Column of Cell"""

        return self.col

    def getValue(self) -> int:
        """Get the Value of Cell"""

        return self.value

    def isLocked(self) -> bool:
        """Check if the Cell is Locked"""

        return self.is_locked

    def setValue(self, value: int) -> None:
        """Set the Value of Cell"""

        self.value = value

    def setLocked(self, locked: bool) -> None:
        """Set whether a Cell should be locked"""

        self.is_locked = locked


class Board:

    def __init__(self) -> None:
        self.arr = [[Cell() for _ in range(9)] for _ in range(9)]
        self.unspecifiedCells = 0

    def getCell(self, row: int, col: int) -> Cell:
        """Get the Cell at a particular coordinate on the board"""

        return self.arr[row][col]

    def validValue(self, row: int, col: int, val: int) -> bool:
        """Check if a value is valid for a particular cell"""

        for r in range(9):
            if r != row and self.getCell(r, col).getValue() == val:
                return False

        for c in range(9):
            if c != col and self.getCell(row, c).getValue() == val:
                return False

        for r in range(((row // 3) * 3), ((row // 3) * 3) + 3):
            for c in range(((col // 3) * 3), ((col // 3) * 3) + 3):
                if r != row and c != col and self.getCell(r, c).getValue() == val:
                    return False

        return True

    def validSolution(self) -> bool:
        """Check if a given solution is valid"""

        for row in range(9):
            for col in range(9):
                if not self.validValue(row, col, self.arr[row][col].getValue()):
                    return False

        return True

    def setCell(self, row: int, col: int, value: int, locked=False) -> None:
        """Set the value of a Cell on the board"""

        self.arr[row][col] = Cell(row, col, value, locked)

    def readFile(self, filename: str) -> None:
        """Read a board file"""

        with open(filename, "r") as file:
            line_list = file.readlines()
            row = 0
            col = 0
            for line in line_list:
                line.strip()
                num_list = line.split(" ")
                for num in num_list:
                    if int(num) == 0:
                        self.arr[row][col] = Cell(row, col, int(num))
                        self.unspecifiedCells += 1
                    else:
                        self.arr[row][col] = Cell(row, col, int(num), True)

                    col += 1
                row += 1
                col = 0

    def __str__(self) -> str:
        """String Representation of a Board"""

        output = f"\n"
        for row in range(9):
            for col in range(9):
                output += f"{self.arr[row][col]} "
                if (col + 1) % 3 == 0:
                    output += f" "

            output += f"\n"
            if (row + 1) % 3 == 0:
                output += f"\n"

        return output


class ListNode:

    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        """String Representation of ListNode"""

        return str(self.val)


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getLast(self):
        """Get the last element in a LinkedList"""

        return self.tail.val

    def getFirst(self):
        """Get the first element in a LinkedList"""

        return self.head.val

    def isEmpty(self):
        """Check whether a LinkedList is empty"""

        return self.size == 0

    def addFirst(self, val):
        """Add item to index 0 of a LinkedList"""

        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head

        new_node = ListNode(val, self.head)
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def addLast(self, val):
        """Add item to the last index of a LinkedList"""

        if not self.tail:
            self.head = ListNode(val)
            self.tail = self.head

        new_node = ListNode(val=val, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def removeFirst(self):
        """Remove item from index 0 of a LinkedList"""

        if not self.head:
            return

        out = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        return out.val

    def removeLast(self):
        """Remove the last item in a LinkedList"""

        if not self.tail:
            return

        out = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

        return out.val


class Stack:

    def __init__(self) -> None:
        self.arr = LinkedList()

    def peek(self):
        """Check the first item to be popped"""

        self.arr.getLast()

    def push(self, item):
        """Add item to Stack"""

        self.arr.addLast(item)

    def pop(self):
        """Remove from the stack"""

        return self.arr.removeLast()

    def isEmpty(self):
        """Check if a stack is empty"""

        return self.arr.isEmpty()

    def size(self):
        """Get the size of the stack"""

        return self.arr.size
