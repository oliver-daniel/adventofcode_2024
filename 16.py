"""Solutions for Day 16."""
import itertools as it
import heapq
from collections import defaultdict, namedtuple
N = open('./in/16.txt').readlines()
# N = open('./in/16.test.txt').readlines()
# N = open('./in/16.test.2.txt').readlines()
# N = open('./in/16.test.debug.txt').readlines()


data = {
    'walls': set(),
    'start': None,
    'end': None
}

H = len(N)
W = len(N[0].strip())

for i, j in it.product(range(H), range(W)):
    match N[i][j]:
        case '.': continue
        case '#':
            data['walls'].add((i, j))
        case 'S':
            data['start'] = (i, j)
        case 'E':
            data['end'] = (i, j)

DEBUG = 1

DIRNS = [
    (0, 1),  # east
    (1, 0),  # south
    (0, -1),  # west
    (-1, 0)  # north
]

HeapItem = namedtuple('Item', 'location direction')


def dijkstras(edges: list[dict[tuple[int, int]]], start=data['start'], start_dirn=0):
    queue: list[tuple[int, HeapItem]] = [(0, HeapItem(start, start_dirn))]
    cheapest_path_to = defaultdict(lambda: float('inf'))
    cheapest_path_to[start] = 0

    prev = defaultdict(lambda: set())

    while queue:
        cost, (location, direction) = heapq.heappop(queue)
        # print(cost, location, direction)
        # 1. can I continue forward?
        if location in edges[direction]:
            hyp_next = edges[direction][location]
            if cost + 1 < cheapest_path_to[hyp_next]:
                cheapest_path_to[hyp_next] = cost + 1
            prev[hyp_next].add(location)
            # Thank you mysterious people of reddit!
            heapq.heappush(
                queue, (cost + 1, HeapItem(hyp_next, direction)))

        # 2. can I turn left?
        left_dirn = (direction - 1) % len(edges)
        if location in edges[left_dirn]:
            hyp_next = edges[left_dirn][location]
            hyp_cost = cost + 1001
            if hyp_cost < cheapest_path_to[hyp_next]:
                cheapest_path_to[hyp_next] = hyp_cost
                prev[hyp_next].add(location)
                heapq.heappush(
                    queue, (hyp_cost, HeapItem(hyp_next, left_dirn)))

        # 3. can I turn right?
        right_dirn = (direction + 1) % len(edges)
        if location in edges[right_dirn]:
            hyp_next = edges[right_dirn][location]
            hyp_cost = cost + 1001
            if hyp_cost < cheapest_path_to[hyp_next]:
                # print('Trying turning right')
                cheapest_path_to[hyp_next] = hyp_cost
                prev[hyp_next].add(location)
                heapq.heappush(
                    queue, (hyp_cost, HeapItem(hyp_next, right_dirn)))

    # for i in range(H):
    #     print("\t".join(str(cheapest_path_to[i, j]) for j in range(W)))
    return cheapest_path_to, prev


def p1(data):
    """My thoughts for approach:
    make a graph of the maze as usual, but divide it into _four different maps_
    based on direction. e.g., one only contains nodes accessible going ^, one 
    only >, etc.
    When the ability exists to 'hop' to a different map at the same point,
    add it as an option at a cost of 1000.
    """

    edges = [dict() for _ in DIRNS]

    for d, dirn in zip(edges, DIRNS):
        di, dj = dirn
        for i, j in it.product(range(1, H - 1), range(1, W - 1)):
            hyp_next = (i + di, j + dj)
            if hyp_next not in data['walls']:
                d[i, j] = hyp_next

    return dijkstras(edges)
    # 143572: too high


def p2(prev):
    """Possible approach:
    Take the result table. Starting on E, flood-fill, splitting the "hydra" as need be, but only including paths which decrease by exactly
    the same amount.
    """

    # for x, y in prev.items():
    #     print(x, y)


if __name__ == "__main__":
    print('--- Part 1 ---')
    cheapest_path, prev = p1(data)
    print(cheapest_path[data['end']])
    print('\n--- Part 2 ---')
    print(p2(prev))
