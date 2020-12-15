from shared import *


def recordLastSpoken(number, turn, dictionary):
    if number not in dictionary:
        dictionary[number] = 0
    else:
        dictionary[number] = turn - dictionary[number]

def feedback(turn, spoken):
    print('turn ' + str(turn) + ': ' + str(spoken))

# Part B... same as A just with a different turn limit
def solveB():
    startingNumbers = split_lines('day15.input')[0].split(',')
    spokenHistory = dict()
    lastSpoken = -1
    turn = 0

    for num in startingNumbers: # these are strings
        turn += 1
        if num not in spokenHistory:
            spokenHistory[num] = []
        spokenHistory[num].append(turn)
        lastSpoken = num

        #feedback(turn, lastSpoken)

    while turn < 30000000:
        turn += 1

        if len(spokenHistory[lastSpoken]) < 2:
            lastSpoken = '0'
        else:
            lastSpoken = str(spokenHistory[lastSpoken][len(spokenHistory[lastSpoken])-1] - spokenHistory[lastSpoken][len(spokenHistory[lastSpoken])-2])

        if lastSpoken not in spokenHistory:
            spokenHistory[lastSpoken] = []
        
        spokenHistory[lastSpoken].append(turn)

        #feedback(turn, lastSpoken)
    return lastSpoken
