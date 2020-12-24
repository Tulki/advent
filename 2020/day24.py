from shared import *

class TileCoord:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addCoord(self, other):
        self.x += other.x
        self.y += other.y

    def toLookupField(self):
        return str(self.x) + ',' + str(self.y)
    
class TileFloor:
    flippedTiles = None

    def __init__(self):
        self.flippedTiles = dict()

    def handleInstruction(self, instruction):
        finalCoord = self.recurseInstruction(instruction)
        lookupField = finalCoord.toLookupField()

        if lookupField not in self.flippedTiles or self.flippedTiles[lookupField] == 'white':
            self.flippedTiles[lookupField] = 'black'
        elif self.flippedTiles[lookupField] == 'black':
            self.flippedTiles[lookupField] = 'white'

    def recurseInstruction(self, remainingInstr):
        if len(remainingInstr) == 0:
            return TileCoord(0,0)
        
        coord = None
        
        if remainingInstr.startswith('nw'):
            coord = TileCoord(-1,1)
        elif remainingInstr.startswith('ne'):
            coord = TileCoord(1,1)
        elif remainingInstr.startswith('e'):
            coord = TileCoord(2,0)
        elif remainingInstr.startswith('se'):
            coord = TileCoord(1,-1)
        elif remainingInstr.startswith('sw'):
            coord = TileCoord(-1,-1)
        elif remainingInstr.startswith('w'):
            coord = TileCoord(-2,0)

        if max(abs(coord.x), abs(coord.y)) == 1:
            charsProcessed = 2
        elif max(abs(coord.x), abs(coord.y)) == 2:
            charsProcessed = 1

        coord.addCoord(self.recurseInstruction(remainingInstr[charsProcessed:]))
        return coord

    def countBlackTiles(self):
        tileStates = [self.flippedTiles[key] for key in self.flippedTiles.keys()]
        return tileStates.count('black')

    def padWhite(self, radius):
        for x in range(radius * 2):
            for y in range(radius * 2):
                coordX = (-1*radius) + x
                coordY = (-1*radius) + y
                coord = TileCoord(coordX, coordY)

                if coord.toLookupField() not in self.flippedTiles:
                    self.flippedTiles[coord.toLookupField()] = 'white'

    def iterateDay(self):
        nextState = dict()

        for key in self.flippedTiles.keys():
            currentColour = self.flippedTiles[key]
            coords = key.split(',')
            x = (int)(coords[0])
            y = (int)(coords[1])
            adjacentBlack = self.countAdjacentBlack(x,y)

            nextState[key] = currentColour
            if currentColour == 'black':
                if adjacentBlack == 0 or adjacentBlack > 2:
                    nextState[key] = 'white'
            else:
                if adjacentBlack == 2:
                    nextState[key] = 'black'

        self.flippedTiles = nextState
    
    def countAdjacentBlack(self, x, y):
        adjacentColours = [
            self.getColourWithWhiteOOB(x+1,y+1), # ne
            self.getColourWithWhiteOOB(x+2,y), # e
            self.getColourWithWhiteOOB(x+1,y-1), # se
            self.getColourWithWhiteOOB(x-1,y-1), # sw
            self.getColourWithWhiteOOB(x-2,y), # w
            self.getColourWithWhiteOOB(x-1,y+1), # nw
        ]
        return adjacentColours.count('black')

    def getColourWithWhiteOOB(self, x, y):
        coord = TileCoord(x, y)
        if coord.toLookupField() not in self.flippedTiles:
            return 'white'
        else:
            return self.flippedTiles[coord.toLookupField()]

# Part A
def solveA():
    inputLines = split_lines('day24.input')
    tileFloor = TileFloor()

    for line in inputLines:
        tileFloor.handleInstruction(line)

    return tileFloor.countBlackTiles()

# Part B
def solveB():
    inputLines = split_lines('day24.input')
    tileFloor = TileFloor()
    tileFloor.padWhite(150)

    for line in inputLines:
        tileFloor.handleInstruction(line)
    for i in range(100):
        day = i+1
        tileFloor.iterateDay()
        print('Day ' + str(day) + ': ' + str(tileFloor.countBlackTiles()))
    
    return tileFloor.countBlackTiles()
