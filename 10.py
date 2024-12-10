"""Solutions for Day 10."""

from collections import defaultdict
import itertools as it


N = open('./in/10.txt').readlines()
# N = open('./in/10.test.txt').readlines()
# N = open('./in/10.test.mini.txt').readlines()


N = [list(map(int, ln.strip())) for ln in N]
H = len(N)
W = len(N[0])

data = defaultdict(set)

for i, j in it.product(range(H), range(W)):
    data[N[i][j]].add((i, j))


DEBUG = 1


def neighbours(i, j, delta=1):
    c = N[i][j]
    for di, dj in [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]:
        new_pos = i + di, j + dj
        if new_pos in data[c + delta]:
            yield new_pos


def p1(data):
    origins = data[0]
    goals = data[9]

    def traverse(curr, seen=None):
        if seen is None:
            seen = set()

        if curr in goals and curr not in seen:
            seen.add(curr)
        else:
            for neighbour in neighbours(*curr):
                traverse(neighbour, seen)

        return seen

    return sum(len(traverse(o)) for o in origins)


def p2(data):
    origins = data[0]
    goals = data[9]

    def traverse(curr):
        if curr in goals:
            return 1
        return sum(
            map(traverse, neighbours(*curr))
        )

    return sum(map(traverse, origins))


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
