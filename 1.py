from collections import Counter

N = open('./in/1.txt').readlines()

data = [tuple(map(int, ln.split())) for ln in N]


def p1(data):
    a, b = map(lambda i: sorted([tup[i] for tup in data]), [0, 1])

    return sum(abs(x - y) for x, y in zip(a, b))


def p2(data):
    a, b = map(lambda i: [tup[i] for tup in data], [0, 1])

    cb = Counter(b)

    return sum(x * cb[x] for x in a)


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
