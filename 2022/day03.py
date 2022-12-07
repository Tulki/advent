from shared import *

def getPriority(item):
    ordinate = ord(item)
    if ordinate >= 97:
        return ordinate - 96
    else:
        return ordinate - 38

class Rucksack:
    contents = None
    compartmentA = None
    compartmentB = None
    
    def __init__(self, contents):
        self.contents = contents
        self.compartmentA = contents[0:int(len(contents)/2)]
        self.compartmentB = contents[int(len(contents)/2):]

    def intersection(self):
        compartAdict = dict()
        for item in self.compartmentA:
            compartAdict[item] = True

        for item in self.compartmentB:
            if item in compartAdict:
                return item

def solveA():
    lines = split_lines('day03.input')

    total_priority = 0
    for line in lines:
        sack = Rucksack(line)
        dupe = sack.intersection()
        priority = getPriority(dupe)
        total_priority = total_priority + priority
    print(total_priority)

class RucksackGroup:
    rucksacks = None

    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def itemCounts(self):
        counts = dict()
        for sack in self.rucksacks:
            for item in sack.contents:
                if item not in counts:
                    counts[item] = 1
                else:
                    counts[item] = counts[item] + 1
        return counts

    def getWithOccurrences(self, occurrences):
        counts = self.itemCounts()
        for key in counts.keys():
            if counts[key] == occurrences:
                return key

def solveB():
    lines = split_lines('day03.input')

    total_priority = 0
    groupCount = 0
    sackGroups = []
    groupSacks = []
    for line in lines:
        sack = Rucksack(line)
        groupSacks.append(sack)
        groupCount += 1
        if groupCount == 3:
            sackGroups.append(RucksackGroup(groupSacks))
            groupSacks = []
            groupCount = 0

    for group in sackGroups:
        tripleItem = group.getWithOccurrences(3)
        groupPriority = getPriority(tripleItem)
        print(tripleItem)
        total_priority += getPriority(tripleItem)

    print(total_priority)
