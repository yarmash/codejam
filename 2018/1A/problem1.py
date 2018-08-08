#!/usr/bin/env python

"""Waffle Choppers"""

from itertools import chain


def check(R, C, H, V, W):
    total_chips = sum(W[r][c] == '@' for r in range(R) for c in range(C))
    pieces = (H + 1) * (V + 1)

    # the total number of chips must be divisible by the number of pieces
    if total_chips % pieces:
        return 'IMPOSSIBLE'

    chips_per_piece = total_chips // pieces

    # each vertical slice must contain chips for H+1 pieces
    vcut_chips = (H + 1)*chips_per_piece
    vcuts = []
    prev_vcut = 0

    for vcut in range(C):
        nchips = 0

        for row in range(R):
            for col in range(prev_vcut, vcut+1):
                nchips += W[row][col] == '@'

        if nchips == vcut_chips:
            vcuts.append(vcut)

            if len(vcuts) == V:
                if total_chips - vcut_chips * len(vcuts) != vcut_chips:
                    return 'IMPOSSIBLE'
                break
            prev_vcut = vcut+1
    else:
        return 'IMPOSSIBLE'

    # each horizontal slice must contain chips for V+1 pieces
    hcut_chips = (V + 1)*chips_per_piece
    hcuts = []
    prev_hcut = 0

    for hcut in range(R):
        nchips = 0
        for col in range(C):
            for row in range(prev_hcut, hcut+1):
                nchips += W[row][col] == '@'

        if nchips == hcut_chips:
            hcuts.append(hcut)
            if len(hcuts) == H:
                if total_chips - hcut_chips * len(hcuts) != hcut_chips:
                    return 'IMPOSSIBLE'
                break
            prev_hcut = hcut+1
    else:
        return 'IMPOSSIBLE'

    # each resulting rectangle must contain exactly the number of chips per piece
    prev_nchips = None
    col = 0
    for vcut in chain(vcuts, [C-1]):  # add explicit cuts at the ends of the grid
        row = 0
        for hcut in chain(hcuts, [R-1]):
            nchips = 0
            for r in range(row, hcut+1):
                for c in range(col, vcut+1):
                    if W[r][c] == '@':
                        nchips += 1
            if prev_nchips is not None and nchips != prev_nchips:
                return 'IMPOSSIBLE'
            prev_nchips = nchips
            row = hcut+1
        col = vcut+1

    return 'POSSIBLE'


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C, H, V = map(int, input().split())  # rows, columns, horizontal cuts, vertical cuts
        W = [input() for _ in range(R)]  # the waffle matrix

        print('Case #{}: {}'.format(case, check(R, C, H, V, W)))


main()
