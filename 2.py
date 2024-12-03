""" COMMENTS:
Part 2 really stumped me. I want to see if there's a more intelligent way of handling the deltas
that would naturally include the ends in a way that I didn't here.
"""

N = open('./in/2.txt').readlines()

data = [list(map(int, ln.split())) for ln in N]


def p1(data):
    safe = 0

    for row in data:
        _sign = 0
        for x, y in zip(row, row[1:]):
            d = y-x
            sign = d // (abs(d) or 1)

            if _sign == 0 and sign != 0:
                _sign = sign
            elif sign != _sign:
                # # print('unsafe: sign change')
                break

            if not 1 <= abs(d) <= 3:
                # # print('unsafe: too big diff')
                break

        else:
            safe += 1
            # # print('safe')
    return safe


def p2(data):
    safe = 0

    def sign(d): return d // (abs(d) or 1)

    def unsafe_indices(row):
        ds = [y-x for x, y in zip(row, row[1:])]

        return [
            i for i, d in enumerate(ds) if
            not (1 <= abs(d) <= 3) or
            (i > 0 and sign(d) != sign(ds[i - 1]))
        ]

    for row in data:
        indices = unsafe_indices(row)

        # print(row, indices)

        if not indices:
            # print("already safe")
            safe += 1
            continue

        for i in indices:
            # print(f'trying without index {i} = {row[:i] + row[i + 1:]}')
            if not unsafe_indices(row[:i] + row[i + 1:]):
                # print("made safe!")
                safe += 1
                break
        else:
            # print(f'Last ditch: remove the ends')
            if not unsafe_indices(row[1:]) or not unsafe_indices(row[:-1]):
                # print("holy! Made safe!")
                safe += 1

            # else:
                # print("couldnt make safe")

    return safe


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
