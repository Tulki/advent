from shared import *
import sys


def extractPassports(passportFile, currPassport):
    # "Flush" passport to recursion output on a blank line or end of file.
    if len(passportFile) == 0:
        return [currPassport]
    line = passportFile[0]
    if line.strip() == '':
        return [currPassport] + extractPassports(passportFile[1:], {})

    keyvals = line.split(' ')
    for keyval in keyvals:
        sep = keyval.split(':')
        currPassport[sep[0]] = sep[1]

    return extractPassports(passportFile[1:], currPassport)

# Part A
def solveA():
    passportFile = split_lines('day04.input')
    
    # im using recursion even if it kills me
    sys.setrecursionlimit(len(passportFile)+2)
    
    passports = extractPassports(passportFile, {})
    numValid = countValidPassportsA(passports)
    print(numValid)

def countValidPassportsA(passportDicts):
    if len(passportDicts) == 0:
        return 0

    if valid_passportA(passportDicts[0]):
        return 1 + countValidPassportsA(passportDicts[1:])
    else:
        return countValidPassportsA(passportDicts[1:])

def valid_passportA(passportDict):
    # cid is the only field that's allowed to be null.
    return('byr' in passportDict) and ('iyr' in passportDict) and ('eyr' in passportDict) and ('hgt' in passportDict) and ('hcl' in passportDict) and ('ecl' in passportDict) and ('pid' in passportDict)


# Part B
def solveB():
    passportFile = split_lines('day04.input')
    
    # im using recursion even if it kills me
    sys.setrecursionlimit(len(passportFile)+2)
    
    passports = extractPassports(passportFile, {})
    numValid = countValidPassportsB(passports)
    print(numValid)

def countValidPassportsB(passportDicts):
    if len(passportDicts) == 0:
        return 0

    if valid_passportB(passportDicts[0]):
        return 1 + countValidPassportsB(passportDicts[1:])
    else:
        return countValidPassportsB(passportDicts[1:])

def valid_passportB(passportDict):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    hexin = digits + ['a','b','c','d','e','f']
    
    # cid is the only field that's allowed to be null.
    if not (('byr' in passportDict) and ('iyr' in passportDict) and ('eyr' in passportDict) and ('hgt' in passportDict) and ('hcl' in passportDict) and ('ecl' in passportDict) and ('pid' in passportDict)):
        return False

    byr = passportDict['byr']
    if len(byr) != 4:
        return False
    if (int)(byr) < 1920 or (int)(byr) > 2002:
        return False
    iyr = passportDict['iyr']
    if len(iyr) != 4:
        return False
    if (int)(iyr) < 2010 or (int)(iyr) > 2020:
        return False
    eyr = passportDict['eyr']
    if len(eyr) != 4:
        return False
    if (int)(eyr) < 2020 or (int)(eyr) > 2030:
        return False

    hgt = passportDict['hgt']
    if hgt.endswith('cm'):
        try:
            hgtint = (int)(hgt[:-2])
            if hgtint < 150 or hgtint > 193:
                return False
        except:
            return False
    elif hgt.endswith('in'):
        try:
            hgtint = (int)(hgt[:-2])
            if hgtint < 59 or hgtint > 76:
                return False
        except:
            return False
    else:
        return False

    # gettin lazy
    hcl = passportDict['hcl']
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    if hcl[1] not in hexin:
        return False
    if hcl[2] not in hexin:
        return False
    if hcl[3] not in hexin:
        return False
    if hcl[4] not in hexin:
        return False
    if hcl[5] not in hexin:
        return False
    if hcl[6] not in hexin:
        return False

    ecl = passportDict['ecl']
    if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    pid = passportDict['pid']
    if len(pid) != 9:
        return False
    # so lazy
    if pid[0] not in digits:
        return False
    if pid[1] not in digits:
        return False
    if pid[2] not in digits:
        return False
    if pid[3] not in digits:
        return False
    if pid[4] not in digits:
        return False
    if pid[5] not in digits:
        return False
    if pid[6] not in digits:
        return False
    if pid[7] not in digits:
        return False
    if pid[8] not in digits:
        return False

    return True
