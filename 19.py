"""Solutions for Day 19."""

from functools import lru_cache


N = open('./in/19.txt').read()
# N = open('./in/19.test.txt').read()

tokens, data = N.split('\n\n')
tokens = tokens.split(', ')
data = data.splitlines()


DEBUG = 1


@lru_cache(maxsize=None)
def ways_to_spell_cached(target, tokens=frozenset(tokens)):
    return 1 if not target else sum(
        map(
            lambda token: ways_to_spell_cached(target[len(token):]),
            filter(lambda token: target.startswith(token), tokens)
        )
    )


def p1(data):
    return sum(1 for result in map(ways_to_spell_cached, data) if result)


def p2(data):
    return sum(map(ways_to_spell_cached, data))


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
