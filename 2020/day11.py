from shared import *

class SeatingArrangement:
    seatRows = []
    stable = False

    def __init__(self, seatRows):
        self.seatRows = seatRows

    def pretty(self):
        for row in self.seatRows:
            print(row)
    
    # 1 if this cell is occupied, 0 otherwise
    def isCellOccupied(self, row, col):
        # Treat any cell outside the boundary as empty floor.
        if row < 0 or row >= len(self.seatRows) or col < 0 or col >= len(self.seatRows[0]):
            return 0
        
        cell = self.seatRows[row][col]
        if cell == '.' or cell == 'L':
            return 0
        else:
            return 1

    # Count all adjacent occupied cells, can be anywhere from 0 to 8.
    def countOccupiedAdjacent(self, row, col):
        n  = self.isCellOccupied(row-1, col)
        ne = self.isCellOccupied(row-1, col+1)
        e  = self.isCellOccupied(row, col+1)
        se = self.isCellOccupied(row+1, col+1)
        s  = self.isCellOccupied(row+1, col)
        sw = self.isCellOccupied(row+1, col-1)
        w  = self.isCellOccupied(row, col-1)
        nw = self.isCellOccupied(row-1, col-1)

        return n+ne+e+se+s+sw+w+nw

    def castVisionRay(self, atRow, atCol, rowStep, colStep):
        atRow += rowStep
        atCol += colStep

        # If the ray goes out of bounds, there is not a visible occupied seat in this direction.
        if atRow < 0 or atRow >= len(self.seatRows) or atCol < 0 or atCol >= len(self.seatRows[0]):
            return 0

        cell = self.seatRows[atRow][atCol]
        if cell == 'L':
            return 0
        elif cell == '#':
            return 1
        else:
            return self.castVisionRay(atRow, atCol, rowStep, colStep)

    def countVisibleOccupied(self, row, col):
        n  = self.castVisionRay(row, col, -1, 0)
        ne = self.castVisionRay(row, col, -1, 1)
        e  = self.castVisionRay(row, col, 0, 1)
        se = self.castVisionRay(row, col, 1, 1)
        s  = self.castVisionRay(row, col, 1, 0)
        sw = self.castVisionRay(row, col, 1, -1)
        w  = self.castVisionRay(row, col, 0, -1)
        nw = self.castVisionRay(row, col, -1, -1)

        return n+ne+e+se+s+sw+w+nw

    def iterateCellA(self, row, col):
        cellVal = self.seatRows[row][col]
        if cellVal == '.':
            return '.'
        elif cellVal == 'L' and self.countOccupiedAdjacent(row, col) == 0:
            return '#'
        elif cellVal == '#' and self.countOccupiedAdjacent(row, col) >= 4:
            return 'L'
        else:
            return cellVal

    def iterateA(self):
        self.stable = True
        nextState = []
        for row in range(len(self.seatRows)):
            nextState.append('')
            for col in range(len(self.seatRows[0])):
                nextCellState = self.iterateCellA(row, col)
                if nextCellState != self.seatRows[row][col]:
                    self.stable = False
                nextState[row] += nextCellState

        self.seatRows = nextState

    def iterateCellB(self, row, col):
        cellVal = self.seatRows[row][col]
        if cellVal == '.':
            return '.'
        elif cellVal == 'L' and self.countVisibleOccupied(row, col) == 0:
            return '#'
        elif cellVal == '#' and self.countVisibleOccupied(row, col) >= 5:
            return 'L'
        else:
            return cellVal

    def iterateB(self):
        self.stable = True
        nextState = []
        for row in range(len(self.seatRows)):
            nextState.append('')
            for col in range(len(self.seatRows[0])):
                nextCellState = self.iterateCellB(row, col)
                if nextCellState != self.seatRows[row][col]:
                    self.stable = False
                nextState[row] += nextCellState

        self.seatRows = nextState
    
    def countOccupied(self):
        occupied = 0
        for row in self.seatRows:
            occupied += row.count('#')
        return occupied

# Part A
def solveA():
    seatRows = split_lines('day11.input')
    arrangement = SeatingArrangement(seatRows)

    while not arrangement.stable:
        arrangement.iterateA()
    return arrangement.countOccupied()

# Part B
def solveB():
    seatRows = split_lines('day11.input')
    arrangement = SeatingArrangement(seatRows)

    while not arrangement.stable:
        arrangement.iterateB()
    return arrangement.countOccupied()
