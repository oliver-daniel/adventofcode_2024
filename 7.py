"""Solutions for Day 7."""

N = open('./in/7.txt').readlines()
# N = open('./in/7.test.txt').readlines()

data = [
    (int(tot), list(map(int, tokens.split()))) for tot, tokens in (
        ln.split(': ') for ln in N
    )
]

DEBUG = 1


OPS = [
    ('+', lambda head, tot, tokens: (True, tokens, tot - head)),
    ('*', lambda head, tot, tokens: (tot % head == 0, tokens, tot // head)),
    # urgh this is gonna need a target instead of a tot
    ('||', lambda head, tot, tokens: (len(tokens) > 0, 
                                      len(tokens) > 0 and tokens[:-1] +
                                      [int(f'{tokens[-1]}{head}')],
                                      tot))
]


def search(tokens: list[int], tot: int, path: list[str], ops):
    if len(tokens) == 0:
        if tot == 0:
            yield path
        return
    *rest, head = tokens
    if head > tot:
        return
    for symbol, f in ops:
        predicate, next_tokens, next_tot = f(head, tot, rest)
        if predicate:
            yield from search(next_tokens, next_tot, path + [symbol], ops)


def p1(data):

    return sum(
        tot for tot, tokens in data if any(search(tokens, tot, [], OPS[:2]))
    )


def p2(data):
    # TODO: wrong
    return sum(
        tot for tot, tokens in data if any(search(tokens, tot, [], OPS))
    )


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
