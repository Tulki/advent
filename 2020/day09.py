from shared import *

class EncodingChecker:
    preamble_length = 25
    preamble = []
    sums = []

    def __init__(self, preamble_length):
        self.preamble_length = preamble_length
        self.preamble = []
        self.sums = []

    def checkAddElement(self, element):
        validElement = True
        # If we've already filled up the preamble, we need to check the new value and then rotate it in if valid.
        if len(self.preamble) == self.preamble_length:
            validElement = self.validElement(element)
            self.preamble = self.preamble[1:]
            self.sums = self.sums[1:]

        self.preamble = self.preamble + [element]
        self.sums = self.sums + [[]]
        for i in range(len(self.preamble)-1):
            self.sums[i] = self.sums[i] + [self.preamble[i] + element]

        return validElement

    def validElement(self, newElement):
        flattenedSums = [elem for sublist in self.sums for elem in sublist]
        return (newElement in flattenedSums)

# Part A
def solveA():
    elements = split_lines('day09.input')
    checker = EncodingChecker(25)
    
    for elem in elements:
        asInt = (int)(elem)
        valid = checker.checkAddElement(asInt)
        if not valid:
            return asInt

# Part B
def solveB():
    elements = split_lines('day09.input')
    invalidNumber = solveA()

    weaknessSifter = [(int)(elements[0])]
    elements = elements[1:]

    while sum(weaknessSifter) != invalidNumber:
        if sum(weaknessSifter) < invalidNumber:
            weaknessSifter = weaknessSifter + [(int)(elements[0])]
            elements = elements[1:]
        else:
            weaknessSifter = weaknessSifter[1:]

    return min(weaknessSifter) + max(weaknessSifter)
    return
