from shared import *


def waitTime(earliestTime, busID):
    rem = earliestTime % busID
    if rem > 0:
        return busID - rem
    return rem

# Part A
def solveA():
    schedule = split_lines('day13.input')
    earliestTime = (int)(schedule[0])
    busIDs = [(int)(x) for x in schedule[1].split(',') if x != 'x']

    waitTimes = [waitTime(earliestTime, busID) for busID in busIDs]
    minWait = min(waitTimes)
    minBusID = busIDs[waitTimes.index(minWait)]

    return minWait * minBusID


# Part B
def checkOffset(time, busID, offset):
    if busID == 'x':
        return True
    return (time + offset) % busID == 0

def checkOffsets(time, busIDs):
    offsetChecks = []
    for i in range(len(busIDs)):
        check = checkOffset(time, busIDs[i], i)
        if not check:
            # Short circuiting will save us time.
            return False

    return True

def solveB():
    schedule = split_lines('day13.input')
    busIDs = ['x' if busID == 'x' else (int)(busID) for busID in schedule[1].split(',')]

    # Skipping timestamps based on the highest bus ID will save us time.
    maxBusID = max([busID for busID in busIDs if busID != 'x'])
    offsetOfMax = busIDs.index(maxBusID)
    
    time = 0
    iteration = 0
    correctOffsets = False
    while not correctOffsets:
        iteration += 1
        time = (iteration * maxBusID) - offsetOfMax
        if (iteration % 1000000) == 0:
            print(time)
        correctOffsets = checkOffsets(time, busIDs)
    return time
