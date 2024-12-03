"""Solutions for Day 3.
Sneaky newlines...
"""
import re

N = open('./in/3.txt').read()
# N = open('./in/3.test.txt').read()
# N = open('./in/3.test.2.txt').read()


data = N
DEBUG = 1

MUL_PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'


def p1(data):
    pattern = re.compile(MUL_PATTERN)

    return sum(int(x) * int(y)
               for x, y in re.findall(pattern, data))


def p2(data):
    patterns = re.compile(rf'(do|don\'t)\(\)|{MUL_PATTERN}')

    t = 0
    ignore = False
    for op, *args in re.findall(patterns, data):
        match op:
            case '':  # mul
                if not ignore:
                    x, y = map(int, args)
                    t += x*y
            case "don't":
                ignore = True
            case "do":
                ignore = False

    return t


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
