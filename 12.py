"""Solutions for Day 12."""
import itertools as it

N = open('./in/12.txt').readlines()
# N = open('./in/12.test.txt').readlines()
# N = open('./in/12.test.mini.txt').readlines()
# N = open('./in/12.test.1.txt').readlines()


DEBUG = 1
data = list(map(str.strip, N))
H = len(data)
W = len(data[0])


def neighbours(i, j):
    for di, dj in [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < H and 0 <= j2 < W:
            yield i2, j2
        else:
            yield None


Region = set[int, int]
RegionSet = dict[str, list[Region]]


def flood_fill(i, j, fill=None) -> Region:
    target = data[i][j]
    if fill is None:
        fill = {(i, j)}
    for posn in neighbours(i, j):
        if posn is None or posn in fill:
            continue
        n_i, n_j = posn
        if data[n_i][n_j] == target:
            fill |= flood_fill(n_i, n_j, fill | {posn})
    return fill


def perimeter(region: Region):
    t = 0
    for i, j in region:
        for neighbour in neighbours(i, j):
            if neighbour is None or neighbour not in region:
                t += 1

    return t


def p1(data):
    regions: RegionSet = {}

    for i, j in it.product(range(H), range(W)):
        target = data[i][j]
        if target not in regions:
            regions[target] = []
        if any((i, j) in region for region in regions[target]):
            continue
        regions[target].append(flood_fill(i, j))

    return sum(
        len(region) * perimeter(region)
        for value in regions.values()
        for region in value
    )


def p2(data):
    """How I might tackle it:
    If a cell only has one side exposed:
      it's part of an ongoing wall. continue.
    If a cell has two sides exposed:
      1. __| - a corner. Stop counting one side and start counting another.
      2. | | - middle. Only count one side; we'll get to the other one later.
    3:
      1. |_| - peninsula. Treat like a corner and prepare to go around.
    4.
      Just a box. Return 4 immediately.
    """


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
