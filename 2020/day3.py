from shared import *

# Part A and B
def solveA():
    slopeMap = split_lines('day3.input')
    result = recurse(slopeMap, 0, 3, 1)
    print(result)

def solveB():
    slopeMap = split_lines('day3.input')
    result1 = recurse(slopeMap, 0, 1, 1)
    result2 = recurse(slopeMap, 0, 3, 1)
    result3 = recurse(slopeMap, 0, 5, 1)
    result4 = recurse(slopeMap, 0, 7, 1)
    result5 = recurse(slopeMap, 0, 1, 2)
    result = result1*result2*result3*result4*result5
    print(result)

def recurse(slopeMap, xCurrent, xJump, yJump):
    if len(slopeMap) == 0:
        return 0
    
    line = slopeMap[0]
    xNext = (xCurrent + xJump) % len(line)

    if line[xCurrent] == '#':
        return 1 + recurse(slopeMap[yJump:], xNext, xJump, yJump)
    else:
        return recurse(slopeMap[yJump:], xNext, xJump, yJump)
