"""Solutions for Day 17."""

from typing import Literal
from attr import dataclass


N = open('./in/17.txt').read()
# N = open('./in/17.test.txt').read()
# N = open('./in/17.test.manual.txt').read()
# N = open('./in/17.test.p2.txt').read()

registers, program = N.split('\n\n')

registers = tuple(int(ln.split(': ')[1]) for ln in registers.splitlines())
program = list(map(int, program.split(': ')[1].split(',')))

data = {
    'registers': registers,
    'program': program
}


@dataclass
class Cmd:
    opcode: int
    instr: str  # TODO
    op_mode: Literal['literal', 'combo', 'ignore']
    seek: int = 2


DEBUG = 1

OPS = {
    0: Cmd(0, 'adv', 'combo'),
    1: Cmd(1, 'bxl', 'literal'),
    2: Cmd(2, 'bst', 'combo'),
    3: Cmd(3, 'jnz', 'literal'),
    4: Cmd(4, 'bxc', 'ignore'),
    5: Cmd(5, 'out', 'combo'),
    6: Cmd(6, 'bdv', 'combo'),
    7: Cmd(7, 'cdv', 'combo')
}

Register = Literal['A', 'B', 'C']


class Program(object):
    def __init__(self, registers: tuple[int, int, int], tape: list[int]):
        self._mem = {
            reg: [value] for reg, value in zip('ABC', registers)
        }

        self._tape = tape
        self.out = []

    def read_register(self, register: Register):
        return self._mem[register][-1]

    def write(self, register: Register, value: int):
        self._mem[register].append(value)

    def read_literal(self, arg: int):
        return arg

    def read_combo(self, arg: int):
        if 0 <= arg <= 3:
            return arg
        elif arg == 7:
            raise Exception('Combo arg 7 read')
        idx = 'ABC'[arg - 4]
        return self.read_register(idx)

    def exec(self, posn: int) -> int:
        try:
            instr = self._tape[posn]
            arg = self._tape[posn + 1]
        except IndexError:
            DEBUG and print('Out of bounds; halting')
            return 0

        op = OPS[instr]

        if op.op_mode == "combo":
            arg = self.read_combo(arg)
        else:
            arg = self.read_literal(arg)

        match op.instr:
            case 'adv':
                denom = 1 << arg
                self.write('A', self.read_register('A') // denom)
            case 'bxl':
                result = self.read_register('B') ^ arg
                self.write('B', result)
            case 'bst':
                self.write('B', arg % 8)
            case 'jnz':
                if self.read_register('A') != 0:
                    return arg
            case 'bxc':
                result = self.read_register('B') ^ self.read_register('C')
                self.write('B', result)
            case 'out':
                result = arg % 8
                self.out.append(result)
            case 'bdv':
                denom = 1 << arg
                self.write('B', self.read_register('A') // denom)
            case 'cdv':
                denom = 1 << arg
                self.write('C', self.read_register('A') // denom)

        return posn + op.seek

    def run(self, start=0):
        cursor = start
        while cursor < len(self._tape):
            seek = self.exec(cursor)
            yield self.out
            cursor = seek


def p1(data):
    pgm = Program(data['registers'], data['program'])

    for out in pgm.run():
        pass
        # print(out, pgm._mem)

    return ",".join(map(str,pgm.out))


def p2(data):
    """first: the lazy way"""
    import itertools as it
    for i in it.count():
        print(i)
        pgm = Program(data['registers'], data['program'])
        pgm._mem['A'] = [i]

        for out in pgm.run():
            for x, y in zip(out, data['program']):
                if x != y : break
            else:
                if len(out) == len(data['program']):
                    return i
            # if out == data['program']:
                # return i


if __name__ == "__main__":
    print('--- Part 1 ---')
    print(r1 := p1(data))
    print('\n--- Part 2 ---')
    print(p2(data))
