from shared import *

class Notes():
    validValues = dict()
    yourTicket = []
    nearbyTickets = []

    def __init__(self):
        self.validValues = dict()
        self.yourTicket = []
        self.nearbyTickets = []

    def permitRange(self, field, minimum, maximum):
        if field not in self.validValues:
            self.validValues[field] = []
        for i in range(minimum, maximum+1):
            self.validValues[field].append(i)

    def getAllValidNumbers(self):
        validNumberRanges = list(self.validValues.values())
        return [item for sublist in validNumberRanges for item in sublist]

    def validTicket(self, ticket):
        allValidNumbers = self.getAllValidNumbers()
        for num in ticket:
            if num not in allValidNumbers:
                return False
        return True

def ParseNotes(lines):
    notes = Notes()
    i = 0

    # Parse valid field ranges into Notes object.
    while lines[i] != '':
        line = lines[i]
        split = line.split(': ')
        field = split[0]
        ranges = split[1]
        splitRanges = ranges.split(' or ')
        for minMax in splitRanges:
            minimum = minMax.split('-')[0]
            maximum = minMax.split('-')[1]
            notes.permitRange(field, (int)(minimum), (int)(maximum))
        i += 1

    i += 2 # skip blank line and "your ticket:" label
    notes.yourTicket = [(int)(x) for x in lines[i].split(',')]

    i += 3 # skip over your ticket numbers, blank line, and "nearby tickets:" label
    while i < len(lines):
        notes.nearbyTickets.append([(int)(x) for x in lines[i].split(',')])
        i += 1

    return notes
    
# Part A
def solveA():
    lines = split_lines('day16.input')
    notes = ParseNotes(lines)

    errorRate = 0
    allValidNumbers = notes.getAllValidNumbers()
    for ticket in notes.nearbyTickets:
        for number in ticket:
            if number not in allValidNumbers:
                errorRate += number
    return errorRate

# Part B
def solveB():
    lines = split_lines('day16.input')
    notes = ParseNotes(lines)

    # To start, each number could be referring to any of the fields.
    fields = [dict() for i in range(len(notes.yourTicket))]
    for key in list(notes.validValues.keys()):
        for item in fields:
            item[key] = True

    # Use the valid tickets to start eliminating possible fields associated with each number.
    for nearbyTicket in notes.nearbyTickets + [notes.yourTicket]:
        if notes.validTicket(nearbyTicket):
            for i in range(len(nearbyTicket)):
                possibleFields = list(fields[i].keys())
                for field in possibleFields:
                    if nearbyTicket[i] not in notes.validValues[field]:
                        del fields[i][field]

    # Now we incrementally examine which numbers can -only- be one field.
    # If a number slot can only be one field, we can eliminate it as a possibility from all the others.
    finalFields = ['' for i in range(len(fields))]
    eliminated = 0
    while eliminated < len(finalFields):
        for i in range(len(fields)):
            if len(list(fields[i].keys())) == 1:
                keyToEliminate = list(fields[i].keys())[0]
                finalFields[i] = keyToEliminate
                eliminated += 1
                for j in range(len(fields)):
                    if keyToEliminate in list(fields[j].keys()):
                        del fields[j][keyToEliminate]
    
    result = 1
    for i in range(len(finalFields)):
        if finalFields[i].startswith('departure'):
            result *= notes.yourTicket[i]
    return result
