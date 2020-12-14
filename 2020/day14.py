from shared import *


def dec2binStr(decNum, bits):
    if bits == 0:
        return ''
    bitVal = 2 ** (bits - 1)
    if decNum >= bitVal:
        return '1' + dec2binStr(decNum - bitVal, bits - 1)
    else:
        return '0' + dec2binStr(decNum, bits - 1)

def binStr2Dec(bitStr):
    if len(bitStr) == 0:
        return 0
    sigBitVal = 2 ** (len(bitStr) - 1)
    if bitStr[0] == '1':
        return sigBitVal + binStr2Dec(bitStr[1:])
    else:
        return binStr2Dec(bitStr[1:])

def apply_value_mask(bitStr, mask):
    if len(bitStr) == 0:
        return ''
    if mask[0] == 'X':
        return bitStr[0] + apply_value_mask(bitStr[1:], mask[1:])
    else:
        return mask[0] + apply_value_mask(bitStr[1:], mask[1:])

def parse_mask(line):
    return line.split(' = ')[1]

def parse_value(line):
    return (int)(line.split(' = ')[1])

def parse_mem_addr(line):
    split = line.split(' = ')
    addr = split[0][4:]
    addr = addr[:len(addr)-1]
    return (int)(addr)

# Part A
def solveA():
    instructions = split_lines('day14.input')
    mask = 'X' * 36
    mem = []

    for instr in instructions:
        if instr.startswith('mask'):
            mask = parse_mask(instr)
        elif instr.startswith('mem'):
            addr = parse_mem_addr(instr)
            value = parse_value(instr)
            # Dynamically expand mem
            while len(mem) < addr+1:
                mem.append(0)
            valueAsBits = dec2binStr(value, 36)
            masked = apply_value_mask(valueAsBits, mask)
            value = binStr2Dec(masked)
            mem[addr] = value

    return sum(mem)


def apply_addr_mask(bitStr, mask):
    if len(bitStr) == 0:
        return ''
    if mask[0] == '0':
        return bitStr[0] + apply_addr_mask(bitStr[1:], mask[1:])
    elif mask[0] == '1':
        return '1' + apply_addr_mask(bitStr[1:], mask[1:])
    else:
        return 'X' + apply_addr_mask(bitStr[1:], mask[1:])

def split_floating_addr(bitStr):
    if bitStr.count('X') == 0:
        return [bitStr]
    xIndex = bitStr.index('X')
    asZero = bitStr[:xIndex] + '0' + bitStr[xIndex+1:]
    asOne = bitStr[:xIndex] + '1' + bitStr[xIndex+1:]
    return split_floating_addr(asZero) + split_floating_addr(asOne)
    
# Part B
def solveB():
    instructions = split_lines('day14.input')
    mask = '0' * 36
    # address space is too big if we use an array again
    # simulate it with a dictionary and only allocate addresses that are requested
    # addresses will be left as binary strings for this
    mem = dict()

    for instr in instructions:
        if instr.startswith('mask'):
            mask = parse_mask(instr)
        elif instr.startswith('mem'):
            addr = parse_mem_addr(instr)
            value = parse_value(instr)
            binAddr = dec2binStr(addr, 36)
            maskedAddr = apply_addr_mask(binAddr, mask)
            floatedAddrs = split_floating_addr(maskedAddr)
            for addr in floatedAddrs:
                mem[addr] = value

    return sum(mem.values())
