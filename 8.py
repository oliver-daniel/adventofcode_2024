"""Solutions for Day 8."""
import itertools as it
from collections import defaultdict

N = open('./in/8.txt').readlines()
# N = open('./in/8.test.txt').readlines()

N = [ln.strip() for ln in N]
H = len(N)
W = len(N[0])

data = defaultdict(list)

for i, j in it.product(range(H), range(W)):
    if (c := N[i][j]) == '.':
        continue
    data[c].append(complex(i, j))

DEBUG = 0

def p1(data):
    valid = set()
    for frequency, posns in data.items():
        # DEBUG and print(f'Processing {frequency=}')

        for a, b in it.combinations(posns, 2):
            d = b - a
            a1 = a - d
            b1 = b + d

            for posn in [a1, b1]:
                if 0 <= posn.real < W and \
                0 <= posn.imag < H:
                    # DEBUG and print(f'{posn} works')
                    valid.add(posn)
    return len(valid)




def p2(data):
    valid = set()
    for frequency, posns in data.items():
        for a, b in it.combinations(posns, 2):
            d = b - a
            for start, dirn in [(a, -1), (b, +1)]:
                valid.add(start)
                curr = start + (d * dirn)
                while 0 <= curr.real < W and 0 <= curr.imag < H:
                    valid.add(curr)
                    curr += (d * dirn)
    
    if DEBUG:
        for pos in it.product(range(H), range(W)):
            if complex(*pos) in valid:
                print('#', end='')
            else: print(N[pos[0]][pos[1]], end='')
            if pos[1] + 1 == W:
                print()

    return len(valid)


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))

