"""Solutions for Day 15."""
import itertools as it

N = open('./in/15.txt').read()
# N = open('./in/15.test.txt').read()
# N = open('./in/15.test.mini.txt').read()


locs, moves = map(str.splitlines, N.split('\n\n'))
H = len(locs)
W = len(locs[0].strip())

data = {
    'start': None,
    'walls': set(),
    'boxes': set(),
    'moves': "".join(moves)

}

for i, j in it.product(range(H), range(W)):
    match locs[i][j]:
        case '.':
            continue
        case '@':
            data['start'] = (i, j)
            continue
        case '#':
            data['walls'].add((i, j))
            continue
        case 'O':
            data['boxes'].add((i, j))
            continue


DELTAS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

DEBUG = 0


def _pp(data):
    for i in range(H):
        print("".join('#' if (posn := (i, j)) in data['walls']
              else 'O' if posn in data['boxes']
              else '@' if 'curr' in data and posn == data['curr']
              else '.'
              for j in range(W)))


def p1(data):
    boxes = data['boxes']
    curr = data['start']

    for move in data['moves']:
        di, dj = DELTAS[move]
        hyp_loc = curr[0] + di, curr[1] + dj

        if hyp_loc in data['walls']:
            DEBUG and print(f"{hyp_loc} Can't go: would hit wall")
            continue
        elif hyp_loc in boxes:
            DEBUG and print(f"{hyp_loc} Ah shit, here we go")
            would_be_pushed = []
            push_loc = hyp_loc[:]
            while push_loc in boxes:
                would_be_pushed.append(push_loc)
                push_loc = push_loc[0] + di, push_loc[1] + dj
            # and one more
            end = push_loc
            DEBUG and print(would_be_pushed, end)

            if end in data['walls']:
                DEBUG and print("  Can't push: stack ends at a wall")
                continue
            boxes = boxes - {would_be_pushed[0]} | {end}
            DEBUG and print("  Pushed successfully")
        else:
            DEBUG and print(f"{hyp_loc} empty")
        curr = hyp_loc

    # _pp({**data, 'boxes': boxes, 'curr': curr})
    return sum(100 * i + j for i, j in boxes)




def p2(data):
    pass


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
