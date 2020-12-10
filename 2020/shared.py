def hello_world():
    print("hello world")

def split_lines(filename):
    lines = []
    for line in open(filename, 'r'):
        lines.append(line.strip())

    return lines

def split_lines_as_ints(filename):
	lines = []
	for line in open(filename, 'r'):
		lines.append((int)(line.strip()))

	return lines
