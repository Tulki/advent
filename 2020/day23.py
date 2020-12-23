from shared import *

# CupGame implemented using a linked list and lookup table for individual nodes.
class CupGame:
    currentCupNode = None
    minCupNumber = None
    maxCupNumber = None

    # Quick lookup for individual nodes.
    lookupTable = None

    def __init__(self, numArray):
        self.minCupNumber = min(numArray)
        self.maxCupNumber = max(numArray)
        self.lookupTable = dict()
        firstNode = CupNode(numArray[0])
        self.currentCupNode = firstNode
        self.lookupTable[str(numArray[0])] = firstNode

        for num in numArray[1:]:
            nextNode = CupNode(num)
            self.currentCupNode.setNext(nextNode)
            self.currentCupNode = self.currentCupNode.nextNode
            self.lookupTable[str(num)] = nextNode

        self.currentCupNode.setNext(firstNode)
        self.currentCupNode = firstNode

    def pluckThreeCups(self):
        plucked = self.currentCupNode.nextNode
        stitchTo = self.currentCupNode.nextNode.nextNode.nextNode.nextNode
        self.currentCupNode.setNext(stitchTo)

        plucked.nextNode.nextNode.setNext(None)
        return plucked

    def getDestinationCupNode(self, plucked):
        pluckedNums = dict()
        pluckedNums[str(plucked.cupNumber)] = True
        pluckedNums[str(plucked.nextNode.cupNumber)] = True
        pluckedNums[str(plucked.nextNode.nextNode.cupNumber)] = True
        
        currentCupNum = self.currentCupNode.cupNumber

        destinationCup = currentCupNum - 1
        while (str(destinationCup) not in self.lookupTable) or (str(destinationCup) in pluckedNums):
            destinationCup -= 1
            if destinationCup < self.minCupNumber:
                destinationCup = self.maxCupNumber

        destinationCupNode = self.lookupTable[str(destinationCup)]
        return destinationCupNode

    def placePluckedCups(self, afterNode, plucked):
        oldNext = afterNode.nextNode
        afterNode.setNext(plucked)
        plucked.nextNode.nextNode.setNext(oldNext)

    def selectNewCurrentCup(self):
        self.currentCupNode = self.currentCupNode.nextNode

    def move(self):
        plucked = self.pluckThreeCups()
        destinationCupNode = self.getDestinationCupNode(plucked)
        self.placePluckedCups(destinationCupNode, plucked)
        self.selectNewCurrentCup()

    def answerA(self):
        answer = ''
        cupNode = self.lookupTable['1']
        for i in range(len(self.lookupTable.keys())-1):
            cupNode = cupNode.nextNode
            answer += str(cupNode.cupNumber)
        return answer

    def answerB(self):
        answer = 1
        cupNode = self.lookupTable['1']
        answer *= cupNode.nextNode.cupNumber
        answer *= cupNode.nextNode.nextNode.cupNumber
        return answer

class CupNode:
    cupNumber = None
    nextNode = None

    def __init__(self, cupNumber):
        self.cupNumber = cupNumber

    def setNext(self, nextNode):
        self.nextNode = nextNode

# Part A
def solveA():
    inputLines = split_lines('day23.input')
    cupNums = []
    for char in inputLines[0]:
        cupNums.append((int)(char))
    
    game = CupGame(cupNums)

    for i in range(100):
        game.move()

    return game.answerA()

# Part B
def solveB():
    inputLines = split_lines('day23.input')
    cupNums = []
    for char in inputLines[0]:
        cupNums.append((int)(char))

    # Pad input up to 1M entries
    maxNum = max(cupNums)
    while len(cupNums) < 1000000:
        maxNum += 1
        cupNums.append(maxNum)

    game = CupGame(cupNums)

    for i in range(1000000):
        game.move()

    return game
