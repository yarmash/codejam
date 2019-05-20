#!/usr/bin/env python

"""Robot Programming Strategy"""

from itertools import cycle, repeat

BEATEN_BY = {'R': 'P', 'P': 'S', 'S': 'R'}  # what's beaten by what


def make_move(moves):
    moves_set = set(moves)
    if len(moves_set) == 1:
        move = BEATEN_BY[moves[0]]
    elif len(moves_set) == 2:
        if moves_set == {'R', 'P'}:
            move = 'P'
        elif moves_set == {'P', 'S'}:
            move = 'S'
        else:  # {'R', 'S'}
            move = 'R'
    else:  # we are doomed
        move = None
    return move


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        A = int(input())  # the number of adversaries
        programs = [cycle(input()) for _ in repeat(None, A)]
        program = []
        while programs:
            moves = list(map(next, programs))
            move = make_move(moves)
            if move is None:
                break
            program.append(move)
            programs = [p for p, m in zip(programs, moves) if BEATEN_BY[m] != move]
        else:
            print('Case #{}: {}'.format(case, ''.join(program)))
            continue

        print('Case #{}: IMPOSSIBLE'.format(case))


main()
