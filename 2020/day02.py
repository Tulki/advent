from shared import *

# Part A
class PasswordRecord:
    def __init__(self, record):
        # Super lazy garbage parse
        splitrec = record.split(':')
        self.password = splitrec[1].strip()
        policy = splitrec[0].split(' ')
        self.policy_char = policy[1].strip()
        self.policy_min = (int)(policy[0].split('-')[0])
        self.policy_max = (int)(policy[0].split('-')[1])

    def check_policyA(self):
        instances = self.password.count(self.policy_char)
        if instances >= self.policy_min and instances <= self.policy_max:
            return True
        return False

    def check_policyB(self):
        first_match = (self.password[self.policy_min-1] == self.policy_char)
        second_match = (self.password[self.policy_max-1] == self.policy_char)
        return first_match ^ second_match


def solveA():
    records = split_lines('day02.input')
    result = recurseA(records)
    print(result)

def recurseA(records):
    if len(records) == 0:
        return 0
    first = PasswordRecord(records[0])
    if first.check_policyA():
        return 1 + recurseA(records[1:])
    else:
        return recurseA(records[1:])


# Part B
def solveB():
    records = split_lines('day02.input')
    result = recurseB(records)
    print(result)

def recurseB(records):
    if len(records) == 0:
        return 0
    first = PasswordRecord(records[0])
    if first.check_policyB():
        return 1 + recurseB(records[1:])
    else:
        return recurseB(records[1:])
