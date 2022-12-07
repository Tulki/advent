from shared import *

def setupScoreTableA():
    # First key = opponent, second key = you
    table = dict()
    table['A'] = dict()
    table['B'] = dict()
    table['C'] = dict()

    rock = 1
    paper = 2
    scissors = 3
    
    lost = 0
    draw = 3
    won = 6
    
    table['A']['X'] = rock + draw
    table['A']['Y'] = paper + won
    table['A']['Z'] = scissors + lost

    table['B']['X'] = rock + lost
    table['B']['Y'] = paper + draw
    table['B']['Z'] = scissors + won

    table['C']['X'] = rock + won
    table['C']['Y'] = paper + lost
    table['C']['Z'] = scissors + draw

    return table

def solveA():
    score_table = setupScoreTableA()
    lines = split_lines('day02.input')

    score_tally = 0
    for line in lines:
        choices = line.split(' ')
        score = score_table[choices[0]][choices[1]]
        score_tally = score_tally + score
    print(score_tally)

def setupDecisionTableB():
    # First key = code (A, B, or C - indicating opponent's choice)
    # Second key = code (X, Y, or Z - meaning lose, draw, or win)
    # Value = (X, Y, or Z - meaning your choice of rock, paper, or scissors)
    table = dict()
    table['A'] = dict()
    table['B'] = dict()
    table['C'] = dict()

    table['A']['X'] = 'Z'
    table['A']['Y'] = 'X'
    table['A']['Z'] = 'Y'

    table['B']['X'] = 'X'
    table['B']['Y'] = 'Y'
    table['B']['Z'] = 'Z'

    table['C']['X'] = 'Y'
    table['C']['Y'] = 'Z'
    table['C']['Z'] = 'X'

    return table

def solveB():
    score_table = setupScoreTableA()
    decision_table = setupDecisionTableB()
    lines = split_lines('day02.input')

    score_tally = 0
    for line in lines:
        choices = line.split(' ')
        choices[1] = decision_table[choices[0]][choices[1]]
        score = score_table[choices[0]][choices[1]]
        score_tally = score_tally + score
    print(score_tally)
