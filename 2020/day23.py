from shared import *

class CupGame:
    # In 'state', the first element is at 12 o'clock.
    # We will maintain that state[0] is the "current cup".
    state = None
    currentCupIndex = None
    minCupNumber = None
    maxCupNumber = None

    movesPerformed = None

    def __init__(self, orderString):
        self.state = []
        self.currentCupIndex = 0
        self.movesPerformed = 0

        for char in orderString:
            self.state.append((int)(char))

        self.minCupNumber = min(self.state)
        self.maxCupNumber = max(self.state)

    def padUpTo(self, maxValue):
        i = self.maxCupNumber
        while i < maxValue:
            i += 1
            self.state.append(i)
        self.maxCupNumber = max(self.state)
    
    def pluckThreeCups(self):
        threeCups = self.state[1:4]
        self.state = [self.state[0]] + self.state[4:]
        return threeCups

    def getDestinationCupIndex(self):
        currentCup = self.state[0]
        
        destinationCup = currentCup - 1
        while destinationCup not in self.state:
            destinationCup -= 1
            if destinationCup < self.minCupNumber:
                destinationCup = self.maxCupNumber

        return self.state.index(destinationCup)

    def placePluckedCups(self, afterIndex, pluckedCups):
        self.state = self.state[0:afterIndex+1] + pluckedCups + self.state[afterIndex+1:]

    def selectNewCurrentCup(self):
        # We "select" a new current cup by rotating to the next one.
        self.state = self.state[1:] + [self.state[0]]

    def move(self):
        pluckedCups = self.pluckThreeCups()
        destinationCupIndex = self.getDestinationCupIndex()
        self.placePluckedCups(destinationCupIndex, pluckedCups)
        self.selectNewCurrentCup()

        self.movesPerformed += 1

# Part A
def solveA():
    inputLines = split_lines('day23.input')
    game = CupGame(inputLines[0])

    for i in range(100):
        game.move()

    finalState = game.state
    pos1 = finalState.index(1)
    answer = ''
    for i in range(len(finalState)-1):
        probeIndex = (pos1+i+1) % len(finalState)
        answer += (str)(finalState[probeIndex])
    return answer

# Part B
def solveB():
    inputLines = split_lines('day23.input')
    game = CupGame(inputLines[0])
    game.padUpTo(1000000)

    for i in range(1000000):
        game.move()
        if game.movesPerformed % 100 == 0:
            print(game.movesPerformed)
    return game
