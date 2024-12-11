"""Solutions for Day 11."""

from collections import defaultdict


N = open('./in/11.txt').readline()
# N = open('./in/11.test.1.txt').readline()

DEBUG = 1
data = defaultdict(int)

for stone in map(int, N.split()):
    data[stone] += 1


def blink(stns):
    new = defaultdict(int)
    for k, v in stns.items():
        if len(strval := str(k)) % 2 == 0:
            L = len(strval)
            new_left = int(strval[:L // 2])
            new_right = int(strval[L // 2:])

            new[new_left] += v
            new[new_right] += v
        else:
            new[k * 2024 or 1] += v

    return new


def p1(data):
    curr = data
    for _ in range(25):
        curr = blink(curr)

    return sum(curr.values())


def p2(data):
    curr = data
    for _ in range(75):
        curr = blink(curr)

    return sum(curr.values())


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
