"""Solutions for Day 6."""

import itertools as it

N = open('./in/6.txt').readlines()
# N = open('./in/6.test.txt').readlines()

data = list(map(str.strip, N))
H = len(data)
W = len(data[0])


DEBUG = 0

DIRN = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

obstacles: set[tuple[int, int]] = set()
guard_init = None

for i, j in it.product(range(H), range(W)):
    if (cell := data[i][j]) == "#":
        obstacles.add((i, j))
    elif cell == "^":
        guard_init = (i, j)


def p1(data):
    y, x = guard_init
    dirn_i = 0

    seen = set()

    while 0 <= y < H and 0 <= x < W:
        seen.add((y, x))
        dy, dx = DIRN[dirn_i]
        y2, x2 = y + dy, x + dx

        if (y2, x2) in obstacles:
            dirn_i += 1
            dirn_i %= 4
            continue
        y, x = y2, x2

    return len(seen)


def p2(data):
    def traverse(obs: tuple[int, int]):
        y, x = guard_init
        dirn_i = 0

        _obstacles = obstacles | {(obs)}

        seen = set()
        while 0 <= y < H and 0 <= x < W:
            tup = (y, x, dirn_i)
            if tup in seen:
                DEBUG and print(f'{obs=} works!')
                return True
            seen.add(tup)

            dy, dx = DIRN[dirn_i]
            y2, x2 = y + dy, x + dx

            if (y2, x2) in _obstacles:
                dirn_i += 1
                dirn_i %= 4
                continue
            y, x = y2, x2

        return False

    t = 0
    for hyp_obs in it.product(range(H), range(W)):
        if hyp_obs == guard_init:
            continue
        if traverse(hyp_obs):
            t += 1
    return t


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
