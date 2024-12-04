"""Solutions for Day 4."""

import itertools as it
from collections import defaultdict

N = open('./in/4.txt').readlines()
# N = open('./in/4.test.txt').readlines()

data = [list(ln.strip()) for ln in N]
DEBUG = 0

H = len(data)
W = len(data[0])


def h_substr(G, i, j, n):
    return G[i][j: j + n]


def v_substr(G, i, j, n):
    return [
        G[i + v][j]
        for v in range(n)
    ]


def dr_substr(G, i, j, n):
    return [
        G[i + t][j + t]
        for t in range(n)
    ]


def ur_substr(G, i, j, n):
    return [
        G[i - t][j + t]
        for t in range(n)
    ]


def p1(data):
    TARGET = list("XMAS")
    TGT_RV = TARGET[::-1]
    n = len(TARGET)

    c = defaultdict(lambda: 0)
    t = 0
    for i, j in it.product(range(H), range(W)):
        if (cell := data[i][j]) != TARGET[0] and cell != TGT_RV[0]:
            continue
        checks = []

        room_right = j + (n - 1) < W
        room_bottom = i + (n - 1) < H
        room_top = i >= n - 1

        if room_right:
            checks.append(h_substr)
        if room_right and room_bottom:
            checks.append(dr_substr)
        if room_right and room_top:
            checks.append(ur_substr)
        if room_bottom:
            checks.append(v_substr)

        for check in checks:
            if (res := check(data, i, j, n)) == TARGET or res == TGT_RV:
                DEBUG and print((i, j), check.__name__, res)
                c[check.__name__] += 1
                t += 1
        # break
    DEBUG and print(c.items(), sum(c.values()))
    return t


def p2(data):
    TARGET = list("SAM")
    TGT_RV = TARGET[::-1]
    n = len(TARGET)

    t = 0

    def valid(guess):
        return guess == TARGET or guess == TGT_RV

    # general procedure: always check UL corner. If there's room for the whole convolution,
    # check DR at (i, j), then UR at (i + 2, j)

    for i, j in it.product(range(H - 2), range(W - 2)):
        res_ul = dr_substr(data, i, j, n)
        if valid(res_ul) and valid(ur_substr(data, i + 2, j, n)):
            DEBUG and print((i, j))
            t += 1

    return t


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
