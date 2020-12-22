from shared import *
import copy

# Part A
def solveA():
    deckInput = split_lines('day22.input')
    deckInput.append('')
    
    player1 = None
    player2 = None
    deck = None
    for line in deckInput:
        if line.startswith('Player'):
            deck = []
        elif line == '' and player1 is None:
            player1 = deck
        elif line == '' and player2 is None:
            player2 = deck
        else:
            deck.append((int)(line))

    while len(player1) > 0 and len(player2) > 0:
        play1 = player1[0]
        player1 = player1[1:]

        play2 = player2[0]
        player2 = player2[1:]

        if play1 > play2:
            player1.append(play1)
            player1.append(play2)
        else:
            player2.append(play2)
            player2.append(play1)

    # Player 1 win.
    if len(player2) == 0:
        scoreTally = []
        for i in range(len(player1)):
            scoreTally.append((len(player1)-i) * player1[i])
        return sum(scoreTally)
    else:
        scoreTally = []
        for i in range(len(player2)):
            scoreTally.append((len(player2)-i) * player2[i])
        return sum(scoreTally)


# Part B
def solveB():
    deckInput = split_lines('day22.input')
    deckInput.append('')
    
    player1 = None
    player2 = None
    deck = None
    for line in deckInput:
        if line.startswith('Player'):
            deck = []
        elif line == '' and player1 is None:
            player1 = deck
        elif line == '' and player2 is None:
            player2 = deck
        else:
            deck.append((int)(line))

    gameWinner = recursiveCombat(1, copy.deepcopy(player1), copy.deepcopy(player2))

    if gameWinner[0] == "player1":
        scoreTally = []
        for i in range(len(gameWinner[1])):
            scoreTally.append((len(gameWinner[1])-i) * gameWinner[1][i])
        return sum(scoreTally)
    else:
        scoreTally = []
        for i in range(len(gameWinner[1])):
            scoreTally.append((len(gameWinner[1])-i) * gameWinner[1][i])
        return sum(scoreTally)

# Returns a tuple ('winner', deck) where 'winner' is 'player1' or 'player2' and the deck is the winner's deck order.
def recursiveCombat(gameNumber, player1, player2):
    print('=== Game ' + (str)(gameNumber) + ' ===')
    print()
    previousStates = dict()
    roundNumber = 0

    while len(player1) > 0 and len(player2) > 0:
        roundNumber += 1
        print('-- Round ' + (str)(roundNumber) + '(Game ' + (str)(gameNumber) + ') --')
        
        p1State = ', '.join([str(num) for num in player1])
        p2State = ', '.join([str(num) for num in player2])
        print("Player 1's deck: " + p1State)
        print("Player 2's deck: " + p2State)
        state = p1State + ':' + p2State
        
        # win defaults to player1 if this state was encountered previously within this game.
        if state in previousStates:
            return ('player1', player1)
        previousStates[state] = True

        # Draw a card
        play1 = player1[0]
        player1 = player1[1:]
        play2 = player2[0]
        player2 = player2[1:]

        print("Player 1 plays: " + (str)(play1))
        print("Player 2 plays: " + (str)(play2))

        roundWinner = None
        # Sub-game condition
        if len(player1) >= play1 and len(player2) >= play2:
            print("Playing a sub-game to determine the winner...")
            print()
            subgame = recursiveCombat(gameNumber + 1, copy.deepcopy(player1), copy.deepcopy(player2))
            roundWinner = subgame[0]
            print("... anyway, back to game " + (str)(gameNumber) + ".")
        else:
            if play1 > play2:
                roundWinner = "player1"
            else:
                roundWinner = "player2"

        if roundWinner == "player1":
            print("Player 1 wins round " + (str)(roundNumber) + " of game " + (str)(gameNumber) + "!")
            print()
            player1.append(play1)
            player1.append(play2)
        elif roundWinner == "player2":
            print("Player 2 wins round " + (str)(roundNumber) + " of game " + (str)(gameNumber) + "!")
            print()
            player2.append(play2)
            player2.append(play1)
        else:
            raise('unknown round winner')

    # Player 1 game win.
    if len(player2) == 0:
        print("The winner of game " + (str)(gameNumber) + " is player 1!")
        print()
        return ("player1", player1)
    else:
        print("The winner of game " + (str)(gameNumber) + " is player 2!")
        print()
        return ("player2", player2)
