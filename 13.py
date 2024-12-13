"""Solutions for Day 13."""
import itertools as it

N = open('./in/13.txt').read()
# N = open('./in/13.test.txt').read()

eqns = [chunk.split('\n') for chunk in N.split('\n\n')]

data: list[tuple[complex, complex, complex]] = []

for lns in eqns:
    tokens = map(lambda ln: ln.split(': ')[1].split(', '), lns)
    data.append(
        [complex(int(x[2:]), int(y[2:])) for x, y in tokens]
    )

DEBUG = 1


def solve(a, b, prize, mx=101):
    # TODO: proper linalg
    return ((t, v) for t, v in it.product(range(mx), repeat=2)
            if t * a + v * b == prize
            )
    # for t, v in it.product(range(101), repeat=2):
    #     if t * a + v * b == prize:
    #         yield t, v


def p1(data):
    return sum(
        3 * a + 1 * b
        for eqn in data
        for a, b in solve(*eqn)
    )


def p2(data):
    MODIFIER = 10_000_000_000_000
    prize_modifier = complex(MODIFIER, MODIFIER)
    return sum(
        3 * t + 1 * v
        for (a, b, prize) in data
        for t, v in solve(a, b, prize + prize_modifier, MODIFIER)
    )


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
