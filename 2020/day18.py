from shared import *

# Part A
def solveA():
    equations = split_lines('day18.input')
    sumOfResults = 0

    for equation in equations:
        # The input only has single digits as numbers... we can be creatively lazy without spaces.
        sumOfResults += compute(equation)
    return sumOfResults

def compute(equation):
    withoutSpaces = equation.replace(' ', '')
    return operate(0, '+', withoutSpaces)

def operate(leftOperand, operator, equation):
    # Base case, right-side equation is just a digit.
    if len(equation) == 1:
        if operator == '+':
            return leftOperand + (int)(equation)
        else:
            return leftOperand * (int)(equation)

    rightOperand = None
    if equation[0] == '(':
        matchingRightBracket = matchRightBracket(equation)
        rightOperand = compute(equation[1:matchingRightBracket])
        equation = equation[matchingRightBracket+1:]
    else:
        # Creative laziness since input only has single digit numbers.
        rightOperand = (int)(equation[0])
        equation = equation[1:]

    result = None
    if operator == '+':
        result = leftOperand + rightOperand
    else:
        result = leftOperand * rightOperand

    if len(equation) == 0:
        return result
    else:
        nextOperator = equation[0]
        return operate(result, nextOperator, equation[1:])

def matchRightBracket(string):
    openBrackets = 1
    index = 0
    while openBrackets > 0:
        index += 1
        char = string[index]
        if char == '(':
            openBrackets += 1
        elif char == ')':
            openBrackets -= 1
    return index


# Part B
def solveB():
    equations = split_lines('day18.input')
    sumOfResults = 0

    for equation in equations:
        # This is the same except we just pre-process the input so addition is prioritized in brackets.
        additionPrioritized = transformEquationForAdditionPriority(equation)
        sumOfResults += compute(additionPrioritized)
    return sumOfResults

def transformEquationForAdditionPriority(equation):
    withoutSpaces = equation.replace(' ', '')
    withBrackets = insertAdditionBrackets(withoutSpaces)
    return withBrackets.replace('_', '+')

def insertAdditionBrackets(equation):
    if equation.count('+') == 0:
        return equation
    
    firstPlus = equation.find('+')
    i = firstPlus
    openBrackets = 0

    # Scan backwards for insertion point.
    while True:
        i -= 1
        if equation[i] == ')':
            openBrackets += 1
        elif equation[i] == '(':
            openBrackets -= 1

        if i == 0 or openBrackets == 0:
            break

    insertBefore = i

    i = firstPlus
    openBrackets = 0
    # Scan forwards for insertion point.
    while True:
        i += 1
        if equation[i] == '(':
            openBrackets += 1
        elif equation[i] == ')':
            openBrackets -= 1

        if i == len(equation)-1 or openBrackets == 0:
            break

    insertAfter = i

    result = equation[:insertBefore] + '(' + equation[insertBefore:firstPlus] + '_' + equation[firstPlus+1:insertAfter+1] + ')' + equation[insertAfter+1:len(equation)]
    return insertAdditionBrackets(result)

    
