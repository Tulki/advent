from shared import *

# Part A
def solveA():
    passes = split_lines('day5.input')
    maxID = recursiveMaxSeatID(passes)
    print(maxID)

def seatID(row, col):
    return row * 8 + col

def recursiveMaxSeatID(passes):
    if len(passes) == 0:
        return -1

    currPass = passes[0]
    rows = [row for row in range(128)]
    cols = [col for col in range(8)]

    passID = findPassID(currPass, rows, cols)
    return max(passID, recursiveMaxSeatID(passes[1:]))

def findPassID(passString, rows, cols):
    if len(passString) == 0:
        return seatID(rows[0], cols[0])

    halfrows = (int)(len(rows) / 2)
    halfcols = (int)(len(cols) / 2)
    
    # Lower half of rows
    if passString[0] == 'F':
        return findPassID(passString[1:], rows[:halfrows], cols)
    # Upper half of rows
    elif passString[0] == 'B':
        return findPassID(passString[1:], rows[halfrows:], cols)
    # Lower half of cols
    elif passString[0] == 'L':
        return findPassID(passString[1:], rows, cols[:halfcols])
    # Upper half of cols
    elif passString[0] == 'R':
        return findPassID(passString[1:], rows, cols[halfcols:])
    else:
        raise('unknown pass character: ' + passString[0])

# Part B
def solveB():
    passes = split_lines('day5.input')
    allSeatIDs = [seatID for seatID in range(seatID(127, 7))]
    guessWho = recursiveElimination(allSeatIDs, passes)

    # Strip away the sequence of unclaimed seats at the front.
    while guessWho[0] is not None:
        guessWho.pop(0)
    # Strip away the sequence of claimed seats after that.
    while guessWho[0] is None:
        guessWho.pop(0)
    # The unclaimed seat immediately following this is ours.
    print(guessWho.pop(0))

def recursiveElimination(remainingSeatIDs, passes):
    if len(passes) == 0:
        return remainingSeatIDs
    
    currPass = passes[0]
    rows = [row for row in range(128)]
    cols = [col for col in range(8)]

    passID = findPassID(currPass, rows, cols)
    remainingSeatIDs[passID] = None
    return recursiveElimination(remainingSeatIDs, passes[1:])
