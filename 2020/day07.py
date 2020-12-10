from shared import *

class MemoizedBagInspector:
    containsMap = {}
    memoizedCounts = {}
    
    def __init__(self, bagRules):
        self.containsMap = {}
        self.memoizedGoldCounts = {}
        
        for line in bagRules:
            split = line.split(" bags contain ")
            container = split[0]
            self.containsMap[container] = []
            contents = split[1]
            if "no other bags" not in contents:
                bagTypes = contents.split(', ')
                for bagType in bagTypes:
                    num = (int)(bagType[0])
                    colour = bagType[1:]
                    colour = colour[:colour.index('bag')].strip()
                    for i in range(num):
                        self.containsMap[container].append(colour)

    def howManyOf(self, countColour, inColour):
        if countColour == inColour:
            return 1

        if countColour not in self.memoizedCounts:
            self.memoizedCounts[countColour] = {}

        if inColour in self.memoizedCounts[countColour]:
            return self.memoizedCounts[countColour][inColour]

        contents = self.containsMap[inColour]
        totalCountColour = 0
        for bag in contents:
            totalCountColour = totalCountColour + self.howManyOf(countColour, bag)

        self.memoizedCounts[countColour][inColour] = totalCountColour
        return totalCountColour

# Part A
def solveA():
    bagRules = split_lines('day07.input')
    inspector = MemoizedBagInspector(bagRules)
    answer = 0
    for line in bagRules:
        bag = line[:line.find(' bags')]
        # For this we do not want to count a shiny gold bag as being a bag that carries shiny gold bags.
        if bag != 'shiny gold':
            shinyGolds = inspector.howManyOf('shiny gold', bag)
            if shinyGolds > 0:
                answer = answer + 1
    print(answer)

# Part B
# Ends up being pretty much an inversion of part A, but we're including total counts instead of just > 0 counts.
def solveB():
    bagRules = split_lines('day07.input')
    inspector = MemoizedBagInspector(bagRules)
    answer = 0
    for line in bagRules:
        bag = line[:line.find(' bags')]
        # Again here we do not want to count shiny gold bags inside our shiny gold bag.
        if bag != 'shiny gold':
            countOfThisBag = inspector.howManyOf(bag, 'shiny gold')
            answer = answer + countOfThisBag
    print(answer)


