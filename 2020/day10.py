from shared import *

# Part A
def solveA():
    adapters = sorted(split_lines_as_ints('day10.input'))
    adapters = adapters + [max(adapters)+3]
    joltDiffs = [0,0,0,0] # number of 0,1,2,3 jolt diffs
    joltDiffs = tallyJoltDiffs(adapters, 0, joltDiffs)
    return joltDiffs[1] * joltDiffs[3]
    
def tallyJoltDiffs(adapters, joltsIn, joltDiffs):
    if len(adapters) == 0:
        return joltDiffs

    nextAdapter = adapters[0]
    diff = nextAdapter - joltsIn
    joltDiffs[diff] = joltDiffs[diff] + 1

    return tallyJoltDiffs(adapters[1:], nextAdapter, joltDiffs)


# Part B
def solveB():
    adapters = sorted(split_lines_as_ints('day10.input'))
    adapters = adapters + [max(adapters)+3]

    # This is too expensive unless we memoize the recursion results.
    # We will memoize where memoizedConfigTallies[len(adapters)-1] = the result for this call
    memoizedConfigTallies = [-1 for x in range(len(adapters)+1)]
    
    return tallyAdapterConfigs(adapters, 0, memoizedConfigTallies)

def tallyAdapterConfigs(adapters, joltsIn, memoizedConfigTallies):
    if len(adapters) == 0:
        return 1

    if memoizedConfigTallies[len(adapters)] > 0:
        return memoizedConfigTallies[len(adapters)]

    possibleAdapters = [x for x in adapters if x-joltsIn < 4]

    possibleConfigs = 0
    for i in range(len(possibleAdapters)):
        possibleConfigs = possibleConfigs + tallyAdapterConfigs(adapters[i+1:], possibleAdapters[i], memoizedConfigTallies)

    memoizedConfigTallies[len(adapters)] = possibleConfigs
    return possibleConfigs
