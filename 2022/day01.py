from shared import *

def solveA():
    calories = split_lines_as_ints('day01.input')
    elves = split_list(calories, '')

    max_cal = 0
    for elf in elves:
        elfsum = sum(elf)
        max_cal = max(max_cal, elfsum)
    
    print(max_cal)

def solveB():
    calories = split_lines_as_ints('day01.input')
    elves = split_list(calories, '')

    elfsums = [sum(x) for x in elves]
    elfsums.sort(reverse=True)
    print(elfsums[0] + elfsums[1] + elfsums[2])
