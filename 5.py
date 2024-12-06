"""Solutions for Day 5."""

from collections import defaultdict


N = open('./in/5.txt').read()
# N = open('./in/5.test.txt').read()

rules, data = N.split('\n\n')

rules = [
    tuple(map(int, ln.split('|')))
    for ln in rules.splitlines()
]

rules_dict = defaultdict(set)

for before, after in rules:
    rules_dict[before].add(after)

data = [
    list(map(int, ln.split(',')))
    for ln in data.splitlines()
]

DEBUG = 1


def partition_valid(data):
    valid, invalid = [], []

    for ln in data:
        seen = set()

    # if any values in rules_dict[X] are already
    # in seen, then we've violated a rule

        for page in ln:
            check = rules_dict[page] & seen
            is_valid = page not in rules_dict or not check
            if not is_valid:
                invalid.append(ln)
                break

            seen.add(page)
        else:
            valid.append(ln)
    return valid, invalid


def p1(data):
    return sum(
        ln[len(ln) // 2]
        for ln in data
    )


def p2(data):
    # observation: exactly one page of each line will always
    # have rules_dict[page] & set(ln) == {}.
    """assert all(
        len([
            page for page in ln if not rules_dict[page] & set(ln)
        ]) == 1
        for ln in data
    )"""

    # This will be our last page. Then, the second-last
    # page will be one whose rules_dict[page] & set(ln) <= {last_page},
    # and so on.

    # BOY did I feel smart for figuring this one out first try.

    t = 0

    for ln in data:
        tokens = set(ln)

        pages_reverse = []
        while len(pages_reverse) < len(tokens):
            candidate = next(
                page for page in ln if
                page not in pages_reverse and
                rules_dict[page] & tokens <= set(pages_reverse)
            )
            "assert len(candidates) == 1"
            pages_reverse.append(candidate)
        t += pages_reverse[len(pages_reverse) // 2]

    return t


def p2_oneline(data):
    from functools import reduce
    return sum(
        (k := reduce(lambda acc, _: acc + [next(
            page for page in ln if
            page not in acc and
            rules_dict[page] & set(ln) <= set(acc)
        )], ln, []))[len(k) // 2]
        for ln in data
    )


if __name__ == "__main__":
    valid, invalid = partition_valid(data)

    print('--- Part 1 ---')
    print(r1 := p1(valid))
    print('\n--- Part 2 ---')
    print(p2(invalid))
    # print(p2_oneline(invalid))
