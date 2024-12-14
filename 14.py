"""Solutions for Day 14."""
from collections import namedtuple, defaultdict
import itertools
from math import prod

N = open('./in/14.txt').readlines()
# N = open('./in/14.test.txt').readlines()

Robot = namedtuple('Robot', 'p v')

data: list[Robot] = []

for ln in N:
    p, v = (tuple(map(int, token[2:].split(','))) for token in ln.split(' '))
    data.append(Robot(p, v))

H = 103
W = 101
DEBUG = 1


def simulate(robot: Robot, tot_time=100):
    (x, y), (dx, dy) = robot

    return (x + (dx * tot_time)) % W, (y + (dy * tot_time)) % H


def _pp(data, H=H, W=W):
    ds = set(data)
    for y in range(H):
        print("".join('#' if (x, y) in ds else '.' for x in range(W)))
        # for y in range(W):
        #     print('#' if (x, y) in ds else '.', end='')
    

def p1(data, H=H, W=W):
    h2 = H // 2
    w2 = W // 2

    t = defaultdict(int)

    for x, y in map(simulate, data):
        if x == w2 or y == h2:
            continue
        t[x > w2, y > h2] += 1

    return prod(t.values())


def p2(data):
    """Looking for the steps with the smallest bounding recs"""

    import itertools as it

    min_area = float('inf')

    for i in it.count():
        results = [simulate(robot, i) for robot in data]
        xs, ys = ([tup[j]for tup in results] for j in range(2))
        (min_x, max_x), (min_y, max_y) = ((min(arr), max(arr)) for arr in [xs, ys])
        
        dx = abs(max_x - min_x)
        dy = abs(max_y - min_y)

        if dx * dy < min_area:
            print('---', i, '---')
            _pp(results)
            min_area = dx * dy

        # as it happens, ...
        if i >= 9000:
            break


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
