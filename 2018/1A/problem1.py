#!/usr/bin/env python

"""Waffle Choppers"""

from itertools import chain, combinations


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C, H, V = map(int, input().split())  # rows, columns, horizontal cuts, vertical cuts

        waffle = [input() for _ in range(R)]
        diners = (H + 1) * (V + 1)

        if sum(waffle[r][c] == '@' for r in range(R) for c in range(C)) % diners:
            print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))
            continue

        print('Case #{}: {}'.format(case, check_combinations(waffle, R, C, H, V)))


def check_combinations(waffle, R, C, H, V):
    for vertical_cuts in combinations(range(1, C), V):
        for horizontal_cuts in combinations(range(1, R), H):
            if check_combination(waffle, R, C, vertical_cuts, horizontal_cuts):
                return 'POSSIBLE'
    return 'IMPOSSIBLE'


def check_combination(waffle, R, C, vertical_cuts, horizontal_cuts):
    """Verify that each piece has the same number of chips"""
    prev_nchips = None
    col = 0
    for vcut in chain(vertical_cuts, (C,)):  # add explicit cuts at the ends of the grid
        row = 0
        for hcut in chain(horizontal_cuts, (R,)):
            nchips = 0
            for r in range(row, hcut):
                for c in range(col, vcut):
                    if waffle[r][c] == '@':
                        nchips += 1
            if prev_nchips is not None and nchips != prev_nchips:
                return False
            prev_nchips = nchips
            row = hcut
        col = vcut
    return True


main()
