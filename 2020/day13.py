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
    correctOffsets = 0
    for i in range(len(busIDs)):
        check = checkOffset(time, busIDs[i], i)
        if not check:
            # Short circuiting will save us time.
            return correctOffsets
        else:
            correctOffsets += 1
    return correctOffsets

def computeLCM(busIDs, correctOffsetCount):
    correctIDs = busIDs[:correctOffsetCount]
    correctIDs = [ID for ID in correctIDs if ID != 'x']
    LCM = 1
    for ID in correctIDs:
        LCM *= ID
    return LCM

def solveB():
    schedule = split_lines('day13.input')
    busIDs = ['x' if busID == 'x' else (int)(busID) for busID in schedule[1].split(',')]

    # Skipping timestamps based on the LCM of checked busIDs will save us time.
    LCM = 1
    
    time = 0
    correctOffsets = 0
    while correctOffsets < len(busIDs):
        time += LCM
        print(time)
        correctOffsets = checkOffsets(time, busIDs)
        newLCM = computeLCM(busIDs, correctOffsets)
        if newLCM > LCM:
            LCM = newLCM
        
    return time
