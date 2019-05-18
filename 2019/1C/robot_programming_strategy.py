#!/usr/bin/env python

"""Robot Programming Strategy"""

from itertools import cycle, repeat


def is_beaten_by(x, y, m={'R': 'P', 'P': 'S', 'S': 'R'}):
    return y == m[x]


def make_move(moves):
    move, beaten = None, []

    for choice in 'RPS':
        if any(is_beaten_by(choice, move) for move in moves):
            continue
        indices = [i for i, move in enumerate(moves) if is_beaten_by(move, choice)]

        if len(indices) > len(beaten):
            beaten = indices
            move = choice
    return move, beaten


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        A = int(input())  # the number of adversaries
        programs = [cycle(input()) for _ in repeat(None, A)]
        program = []
        while programs:
            moves = list(map(next, programs))
            move, beaten = make_move(moves)
            if move is None:
                break
            program.append(move)
            programs = [p for i, p in enumerate(programs) if i not in beaten]
        else:
            print('Case #{}: {}'.format(case, ''.join(program)))
            continue

        print('Case #{}: IMPOSSIBLE'.format(case))


main()
