from shared import *

# Part A
def solveA():
    inputs = split_lines('day19.input')
    rules = dict()

    i = 0
    while inputs[i] != '':
        line = inputs[i]
        key, rule = line.split(':')[0].strip(), line.split(':')[1].strip()
        rules[key] = rule
        i += 1

    messages = []
    for line in inputs[i+1:]:
        messages.append(line)

    validStrings = evaluateRule(rules, rules['0'])

    result = 0
    for message in messages:
        if message in validStrings:
            result += 1

    return result

def evaluateRule(rulesDict, rule):
    if '"' in rule:
        stripChar = rule.replace('"', '')
        return [stripChar]

    elif '|' in rule:
        result = []
        splitORs = rule.split('|')
        for orRule in splitORs:
            result.append(evaluateRule(rulesDict, orRule.strip()))
        return flattenList(result)

    # Else this is a rule without '|' ORs
    else:
        strippedRule = rule.strip()
        result = []
        for subRule in strippedRule.split(' '):
            subRuleStr = rulesDict[subRule]
            result.append(evaluateRule(rulesDict, subRuleStr))
        
        while len(result) > 1:
            result[1] = multiplyLists(result[0], result[1])
            result = result[1:]
        return flattenList(result)

def multiplyLists(listA, listB):
    result = []
    for a in listA:
        for b in listB:
            result.append(a + b)
    return result

def flattenList(listOfLists):
    return [item for sublist in listOfLists for item in sublist]


# Part B
def solveB():
    inputs = split_lines('day19.input')
    rules = dict()

    i = 0
    while inputs[i] != '':
        line = inputs[i]
        key, rule = line.split(':')[0].strip(), line.split(':')[1].strip()
        rules[key] = rule
        i += 1

    messages = []
    for line in inputs[i+1:]:
        messages.append(line)

    # rule 0 is '8 11'
    # meaning '42' one or more times followed by
    # '42' n more times (n > 0) followed by
    # '31' n times

    # valid '42's and '31's are all of length 8. Also they have no intersection between them.
    # skim a '42's from the front until we can no longer match them.
    # then skim '31's until we reach the end.
    # there should be more '42's found than '31's, and we should be able to skim to the end.
    rule42s = evaluateRule(rules, rules['42'])
    rule31s = evaluateRule(rules, rules['31'])

    result = 0
    for message in messages:
        if chkMsgPartB(rule42s, rule31s, 0, 0, message):
            result += 1

    return result

def chkMsgPartB(rule42s, rule31s, skimmed42s, skimmed31s, message):
    if len(message) % 8 != 0:
        return False

    if len(message) == 0:
        return skimmed42s > skimmed31s and skimmed31s > 0

    if message[0:8] in rule42s and skimmed31s == 0:
        return chkMsgPartB(rule42s, rule31s, skimmed42s + 1, skimmed31s, message[8:])

    elif message[0:8] in rule31s:
        return chkMsgPartB(rule42s, rule31s, skimmed42s, skimmed31s + 1, message[8:])

    else:
        return False
