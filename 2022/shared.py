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
        try:
            lines.append(int(line.strip()))
        except ValueError:
            lines.append(line.strip())

    return lines

def split_lines_no_strip(filename):
    lines = []
    for line in open(filename, 'r'):
        lines.append(line)

    return lines

def split_list(lst, delim):
    return list(split_list_helper(lst, delim))

def split_list_helper(lst, delim):
    sublst = []
    for x in lst:
        if x == delim:
            yield sublst
            sublst = []
            continue
        sublst.append(x)
    yield sublst
