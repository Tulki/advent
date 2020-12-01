def checkLengths(a, b, c):
    return ((a+b > c) and (a+c > b) and (b+c > a))

validTriangles = 0

f = open('dataInput.txt', 'r')
for line in f.readlines():
    splitNums = line.split()
    lengths = [int(l) for l in splitNums]

    if (checkLengths(lengths[0], lengths[1], lengths[2])):
        validTriangles += 1

f.close()
print(validTriangles)
