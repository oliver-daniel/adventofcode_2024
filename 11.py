"""Solutions for Day 11."""

from typing import Union


N = open('./in/11.txt').readline()
# N = open('./in/11.test.1.txt').readline()

DEBUG = 1
data = N.strip().split()


class Node(object):
    value: Union[int,  None]
    left: Union['Node',  None]
    right: Union['Node',  None]

    def __init__(self, value: int):
        self.value = int(value)
        self.left = None
        self.right = None

    def __repr__(self):
        if self.value is not None:
            return f'<{self.value}>'
        return f'<[{self.left}, {self.right}]>'


def p1(data):
    def blink(node: Node):
        if node is None:
            return

        if node.value is None:
            blink(node.left)
            blink(node.right)
            return

        if node.value == 0:
            node.value = 1
            return

        if len(strval := str(node.value)) % 2 == 0:
            new_left = Node(strval[:len(strval) // 2])
            new_right = Node(strval[len(strval) // 2:])
            if new_left.value is None:
                print ("uh oh!", strval)
            node.left = new_left
            node.right = new_right
            node.value = None
            return

        node.value *= 2024

    curr = [Node(int(v)) for v in data]
    # print(curr)
    for _ in range(25):
        for node in curr:
            blink(node)
        # print(curr)

    def weight(node: Node):
        if node is None:
            return 0
        if node.value is not None:
            return 1
        return weight(node.left) + weight(node.right)
    
    return sum(map(weight, curr))


def p2(data):
    pass


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
