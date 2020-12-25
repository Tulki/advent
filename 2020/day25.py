from shared import *

def transformSubjectNumber(subject_number, loop_size):
    result = 1
    modulo = 20201227

    for i in range(loop_size):
        result *= subject_number
        result %= modulo

    return result

def reverseTransform(public_key, initial_subject_number):
    modulo = 20201227
    loop_size = 0

    while public_key > 1:
        if public_key % initial_subject_number == 0:
            public_key /= initial_subject_number
            loop_size += 1
        else:
            public_key += modulo

    return loop_size
    

# Part A
def solveA():
    public_keys = split_lines('day25.input')
    card_public_key = (int)(public_keys[0])
    door_public_key = (int)(public_keys[1])

    initial_subject_number = 7

    card_loop_size = reverseTransform(card_public_key, initial_subject_number)
    door_loop_size = reverseTransform(door_public_key, initial_subject_number)

    encryption_key = transformSubjectNumber(card_public_key, door_loop_size)
    return encryption_key
