from shared import *

# Part A
def recurse(entries):
    i = 0
    j = 1

    first = 0
    second = 0

    while (j < len(entries)):
        first = (int)(entries[i])
        second = (int)(entries[j])
        
        if (first + second == 2020):
            return first * second

        j = j + 1
    
    return recurse(entries[1:])

def solveA():
    entries = split_lines('day1.input')
    answer = recurse(entries)
    print(answer)

# Part B
def headCurse(entries):
    if len(entries) == 0:
        return None

    head = (int)(entries[0])
    body = bodyCurse(head, entries[1:])
    if (body is None):
        return headCurse(entries[1:])
    else:
        return head * body

def bodyCurse(head, entries):
    if len(entries) == 0:
        return None

    body = (int)(entries[0])
    tail = tailCurse(head, body, entries[1:])
    if (tail is None):
        return bodyCurse(head, entries[1:])
    else:
        return body * tail

def tailCurse(head, body, entries):
    if len(entries) == 0:
        return None

    tail = (int)(entries[0])
    if (head + body + tail == 2020):
        print("FOUND A MATCH!!!")
        print(head)
        print(body)
        print(tail)
        return tail
    else:
        return tailCurse(head, body, entries[1:])


def solveB():
    entries = split_lines('day1.input')
    answer = headCurse(entries)
    print(answer)

    
