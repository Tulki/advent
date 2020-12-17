from shared import *

class PocketDimension:
    padding = 0 # determines padding around the starting input of the dimension
    state = None

    def __init__(self, padding, inputLines):
        self.padding = padding
        
        xLen = len(inputLines[0]) + 2*padding
        yLen = len(inputLines) + 2*padding
        zLen = 1 + 2*padding

        self.state = []
        for x in range(xLen):
            self.state.append([])
            for y in range(yLen):
                self.state[x].append([])
                for z in range(zLen):
                    self.state[x][y].append('.')

        for y in range(len(inputLines)):
            for x in range(len(inputLines[0])):
                self.state[x+padding][y+padding][padding] = inputLines[y][x]

    def getCube(self, x, y, z):
        # Consider anything outside the bounds of the pocket dimension to be inactive.
        # As long as we pad the input at least as many cells as there are boot cycles, this shouldn't matter.
        if x < 0 or x >= len(self.state) or y < 0 or y >= len(self.state[0]) or z < 0 or z >= len(self.state[0][0]):
            return '.'
        return self.state[x][y][z]

    def setCube(self, x, y, z, state):
        self.state[x][y][z] = state

    def countAdjacentActive(self, x, y, z):
        thisCube = self.getCube(x, y, z)
        adjacentActive = 0
        if thisCube == '#':
            adjacentActive -= 1

        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                for k in range(z-1,z+2):
                    cube = self.getCube(i,j,k)
                    if cube == '#':
                        adjacentActive += 1

        return adjacentActive

    def bootCycle(self):
        newState = []
        for i in range(len(self.state)):
            newState.append([])
            for j in range(len(self.state[i])):
                newState[i].append([])
                for k in range(len(self.state[i][j])):
                    newState[i][j].append('.')
                    thisCube = self.getCube(i,j,k)
                    adjacentActive = self.countAdjacentActive(i,j,k)
                    if thisCube == '#':
                        if adjacentActive == 2 or adjacentActive == 3:
                            newState[i][j][k] = '#'
                        else:
                            newState[i][j][k] = '.'
                    elif thisCube == '.':
                        if adjacentActive == 3:
                            newState[i][j][k] = '#'
                        else:
                            newState[i][j][k] = '.'
                    else:
                        raise('unknown cube state found during boot cycle')
        self.state = newState

    def countActive(self):
        active = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                for k in range(len(self.state[i][j])):
                    if self.state[i][j][k] == '#':
                        active += 1
        return active


# Crappy solution for part B with a fourth dimension stapled on
class PocketDimensionFourth:
    padding = 0 # determines padding around the starting input of the dimension
    state = None

    def __init__(self, padding, inputLines):
        self.padding = padding
        
        xLen = len(inputLines[0]) + 2*padding
        yLen = len(inputLines) + 2*padding
        zLen = 1 + 2*padding
        wLen = 1 + 2*padding

        self.state = []
        for x in range(xLen):
            self.state.append([])
            for y in range(yLen):
                self.state[x].append([])
                for z in range(zLen):
                    self.state[x][y].append([])
                    for w in range(wLen):
                        self.state[x][y][z].append('.')

        for y in range(len(inputLines)):
            for x in range(len(inputLines[0])):
                self.state[x+padding][y+padding][padding][padding] = inputLines[y][x]

    def getCube(self, x, y, z, w):
        # Consider anything outside the bounds of the pocket dimension to be inactive.
        # As long as we pad the input at least as many cells as there are boot cycles, this shouldn't matter.
        if x < 0 or x >= len(self.state) or y < 0 or y >= len(self.state[0]) or z < 0 or z >= len(self.state[0][0]) or w < 0 or w >= len(self.state[0][0][0]):
            return '.'
        return self.state[x][y][z][w]

    def setCube(self, x, y, z, w, state):
        self.state[x][y][z][w] = state

    def countAdjacentActive(self, x, y, z, w):
        thisCube = self.getCube(x, y, z, w)
        adjacentActive = 0
        if thisCube == '#':
            adjacentActive -= 1

        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                for k in range(z-1,z+2):
                    for l in range(w-1,w+2):
                        cube = self.getCube(i,j,k,l)
                        if cube == '#':
                            adjacentActive += 1

        return adjacentActive

    def bootCycle(self):
        newState = []
        for i in range(len(self.state)):
            newState.append([])
            for j in range(len(self.state[i])):
                newState[i].append([])
                for k in range(len(self.state[i][j])):
                    newState[i][j].append([])
                    for l in range(len(self.state[i][j][k])):
                        newState[i][j][k].append('.')
                        thisCube = self.getCube(i,j,k,l)
                        adjacentActive = self.countAdjacentActive(i,j,k,l)
                        if thisCube == '#':
                            if adjacentActive == 2 or adjacentActive == 3:
                                newState[i][j][k][l] = '#'
                            else:
                                newState[i][j][k][l] = '.'
                        elif thisCube == '.':
                            if adjacentActive == 3:
                                newState[i][j][k][l] = '#'
                            else:
                                newState[i][j][k][l] = '.'
                        else:
                            raise('unknown cube state found during boot cycle')
        self.state = newState

    def countActive(self):
        active = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                for k in range(len(self.state[i][j])):
                    for l in range(len(self.state[i][j][k])):
                        if self.state[i][j][k][l] == '#':
                            active += 1
        return active



# Part A
def solveA():
    startingInput = split_lines('day17.input')
    maxCycles = 6
    
    dimension = PocketDimension(maxCycles, startingInput)
    for i in range(6):
        dimension.bootCycle()
    return dimension.countActive()

# Part B
def solveB():
    startingInput = split_lines('day17.input')
    maxCycles = 6
    
    dimension = PocketDimensionFourth(maxCycles, startingInput)
    for i in range(6):
        dimension.bootCycle()
    return dimension.countActive()

