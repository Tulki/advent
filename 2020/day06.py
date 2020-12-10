from shared import *
import sys

# Part A
def solveA():
    declarations = split_lines('day06.input')
    sys.setrecursionlimit(len(declarations)+2)

    answer = countAnyoneYes(declarations, set())
    print(answer)

def countAnyoneYes(declarations, unionSet):
    # End of declarations list, flush the last group's yes count.
    if len(declarations) == 0:
        return len(unionSet)
    line = declarations[0]
    # End of a group in the declarations list, flush the group's yes count and continue.
    if line == '':
        return len(unionSet) + countAnyoneYes(declarations[1:], set())

    for char in line:
        unionSet.add(char)

    return countAnyoneYes(declarations[1:], unionSet)


# Part B
def solveB():
    declarations = split_lines('day06.input')
    sys.setrecursionlimit(len(declarations)+2)

    answer = countAllYes(declarations, fullSet())
    print(answer)

def countAllYes(declarations, intersectionSet):
    # End of declarations list, flush the last group's yes count.
    if len(declarations) == 0:
        return len(intersectionSet)
    line = declarations[0]
    # End of a group in the declarations list, flush the group's yes count and continue.
    if line == '':
        return len(intersectionSet) + countAllYes(declarations[1:], fullSet())

    personSet = set()
    for char in line:
        personSet.add(char)
        
    return countAllYes(declarations[1:], intersectionSet.intersection(personSet))

def fullSet():
    return set(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))
