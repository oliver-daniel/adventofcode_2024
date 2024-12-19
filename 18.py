"""Solutions for Day 18."""
import itertools as it
import heapq
from collections import defaultdict

TEST = 0

if TEST:
    N = open('./in/18.test.txt').readlines()
else:
    N = open('./in/18.txt').readlines()

N = (map(int, ln.split(',')) for ln in N)

H = W = (7 if TEST else 71)

START = 0, 0
END = H - 1, W - 1

data = [(i, j) for j, i in N]

DEBUG = 1

DIRNS = [
    (0, 1),  # east
    (1, 0),  # south
    (0, -1),  # west
    (-1, 0)  # north
]


def dijkstras(obstacles: set[tuple[int, int]], start=START):
    queue = [(0, start)]

    shortest_path_to = defaultdict(lambda: float('inf'))
    shortest_path_to[start] = 0

    # prev = defaultdict(lambda: set())

    while queue:
        cost, (i, j) = heapq.heappop(queue)

        for di, dj in DIRNS:
            if not (0 <= i + di < H and 0 <= j + dj < W):
                continue

            hyp_next = i + di, j + dj

            if hyp_next not in obstacles:
                if cost + 1 < shortest_path_to[hyp_next]:
                    shortest_path_to[hyp_next] = cost + 1
                    heapq.heappush(
                        queue, (cost + 1, hyp_next)
                    )
    return shortest_path_to


def p1(data):
    prefix = 12 if TEST else 1024
    obstacles = set(data[:prefix])
    paths = dijkstras(obstacles)

    return paths[END]


def p2(data):
    for prefix in range(1, len(data)):
        obstacles = set(data[:-prefix])
        paths = dijkstras(obstacles)

        if paths[END] < float('inf'):
            last = data[-prefix]
            return f'{last[1]},{last[0]}'


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
