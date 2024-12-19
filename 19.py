"""Solutions for Day 19."""

from functools import cache, lru_cache


N = open('./in/19.txt').read()
# N = open('./in/19.test.txt').read()

tokens, data = N.split('\n\n')
tokens = tokens.split(', ')
data = data.splitlines()


DEBUG = 1


@lru_cache(maxsize=None)
def ways_to_spell_cached(target, tokens=frozenset(tokens)):
    if not target:
        return 1

    t = 0
    for token in tokens:
        if not target.startswith(token):
            continue
        suffix = target[len(token):]

        if (result := ways_to_spell_cached(suffix, tokens)):
            t += result

    return t


def p1(data):
    return sum(1 for result in map(ways_to_spell_cached, data) if result)


def p2(data):
    return sum(map(ways_to_spell_cached, data))


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
