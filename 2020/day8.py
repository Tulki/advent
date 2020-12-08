from shared import *
import copy

# Part A
def solveA():
    instructions = split_lines('day8.input')
    answer = detectLoop(instructions, 0, 0, set())
    print(answer)

def detectLoop(instructions, instructNum, accumulator, loopDetectorSet):
    # If we run over an instruction for the second time, break and return the acc value.
    if instructNum in loopDetectorSet:
        return accumulator

    loopDetectorSet.add(instructNum)
    
    thisInstr = instructions[instructNum]
    split = thisInstr.split(' ')

    # Default, may be overwritten by jmp ops
    nextInstructNum = instructNum + 1
    
    if split[0] == 'acc':
        accumulator = accumulator + ((int)(split[1]))
    elif split[0] == 'jmp':
        nextInstructNum = instructNum + ((int)(split[1]))
    elif split[0] == 'nop':
        do = 'nothing'
    elif split[0] == 'end':
        print('Reached the end. Acc=' + (str)(accumulator))
        return accumulator

    return detectLoop(instructions, nextInstructNum, accumulator, loopDetectorSet)


# Part B
def solveB():
    instructions = split_lines('day8.input') + ['end +0']
    fixOneInstruction(instructions, 0, 0, set())

# Almost the same as detectLoop, except this can recurse at most once into a regular detectLoop call, with a flipped instruction.
def fixOneInstruction(instructions, instructNum, accumulator, loopDetectorSet):
    # If we run over an instruction for the second time, break and return the acc value.
    if instructNum in loopDetectorSet:
        return accumulator

    loopDetectorSet.add(instructNum)
    
    thisInstr = instructions[instructNum]
    split = thisInstr.split(' ')

    # Default, may be overwritten by jmp ops
    nextInstructNum = instructNum + 1
    
    if split[0] == 'acc':
        accumulator = accumulator + ((int)(split[1]))
    elif split[0] == 'jmp':
        nextInstructNum = instructNum + ((int)(split[1]))
        flippedInstructNum = instructNum + 1
        detectLoop(instructions, flippedInstructNum, accumulator, copy.deepcopy(loopDetectorSet))
    elif split[0] == 'nop':
        flippedInstructNum = instructNum + ((int)(split[1]))
        detectLoop(instructions, flippedInstructNum, accumulator, copy.deepcopy(loopDetectorSet))
    elif split[0] == 'end':
        print('Reached the end. Acc=' + (str)(accumulator))
        return accumulator

    return fixOneInstruction(instructions, nextInstructNum, accumulator, loopDetectorSet)
