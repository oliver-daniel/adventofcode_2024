"""Solutions for Day 23."""
import itertools as it
from collections import defaultdict

N = open('./in/23.txt').readlines()
# N = open('./in/23.test.txt').readlines()

data = defaultdict(set)

for ln in N:
    a, b = ln.strip().split('-')
    data[a].add(b)
    data[b].add(a)

DEBUG = 1


def p1(data):
    tot = set()
    for key, cxns in data.items():
        if not key.startswith('t'):
            continue

        for x, y in it.combinations(cxns, 2):
            if y in data[x]:
                tot.add(frozenset({key, x, y}))

    return len(tot)


def p2(data):
    """Insight: a clique of degree k has exactly k nodes, 
    each with at least k edges.

    Also... you may need to start with smaller cliques
    and see which can survive to the next round.
    """

    def build_cliques(cliques, k):
        """precondition: <cliques> is a set contains existing cliques of size k
           postcondition: return cliques of size k + 1
        """
        candidates = [key for key, v in data.items() if len(v) >= k]

        ret = set()

        for clique in cliques:
            for candidate in candidates:
                if data[candidate] >= clique:
                    ret.add(frozenset(clique | {candidate}))

        return ret

    max_k = max(map(len, data.values()))

    cliques = [{key} for key in data]
    for k in range(1, max_k + 1):
        DEBUG and print(f'Cliques of size {k}: {len(cliques)}')
        cliques = build_cliques(cliques, k + 1)

        if len(cliques) == 1:
            return ",".join(sorted(cliques.pop()))


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
