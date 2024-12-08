"""Solutions for Day 7."""

N = open('./in/7.txt').readlines()
# N = open('./in/7.test.txt').readlines()

data = [
    (int(tot), list(map(int, tokens.split()))) for tot, tokens in (
        ln.split(': ') for ln in N
    )
]

DEBUG = 1

def search(tokens: list[int], tot: int, target: int, path: list[str], with_concat=False):
    if len(tokens) == 0:
        if tot == target:
            yield path
        return
    head, *rest = tokens
    
    yield from search(rest, tot + head, target, path + ['+'], with_concat)
    if len(path) > 0:
        yield from search(rest, tot * head, target, path + ['*'], with_concat)
    if with_concat and len(path) > 0:
        new_head = int(f'{tot}{head}')
        yield from search(rest, new_head, target, path + ['||'], with_concat)



def p1(data):
    return sum(
        target for target, tokens in data if any(search(tokens, 0, target, [], False))
    )


def p2(data):
    return sum(
        target for target, tokens in data if any(search(tokens, 0, target, [], True))
    )


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
