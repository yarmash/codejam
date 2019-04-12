#!/usr/bin/env python

"""Waffle Choppers"""


def calc_cumulative_sums(W, R, C):
    """Calculate cumulative sums for rows and columns of the waffle"""

    S = 0  # total chips
    SR = [0]*R
    SC = [0]*C

    for r in range(R):
        for c in range(C):
            has_chip = W[r][c] == '@'
            S += has_chip
            SR[r] += has_chip
            SC[c] += has_chip

    for i in range(1, len(SR)):
        SR[i] += SR[i-1]

    for i in range(1, len(SC)):
        SC[i] += SC[i-1]

    return SR, SC, S


def check(R, C, H, V, W):
    SR, SC, S = calc_cumulative_sums(W, R, C)

    pieces = (H + 1)*(V + 1)

    # the total number of chips must be divisible by the number of pieces
    if S % pieces:
        return 'IMPOSSIBLE'

    chips_per_hslice = S // (H + 1)
    chips_per_vslice = S // (V + 1)

    # each of the V + 1 vertical slices must have exactly S/(V + 1) chips
    vcuts = []
    next_sum = chips_per_vslice
    for col, col_sum in enumerate(SC):
        if col_sum == next_sum:
            vcuts.append(col)
            if len(vcuts) == V:
                if SC[-1] - next_sum != chips_per_vslice:
                    return 'IMPOSSIBLE'
                break
            next_sum += chips_per_vslice
    else:
        return 'IMPOSSIBLE'

    # each of the H + 1 horizontal slices must have exactly S/(H + 1) chips
    hcuts = []
    next_sum = chips_per_hslice
    for row, row_sum in enumerate(SR):
        if row_sum == next_sum:
            hcuts.append(row)
            if len(hcuts) == H:
                if SR[-1] - next_sum != chips_per_hslice:
                    return 'IMPOSSIBLE'
                break
            next_sum += chips_per_hslice
    else:
        return 'IMPOSSIBLE'

    # each resulting rectangle must contain exactly the number of chips per piece
    chips_per_piece = S // pieces
    # add explicit cuts after the last row/column
    hcuts.append(R-1)
    vcuts.append(C-1)

    prev_col = 0
    for vcut in vcuts:
        prev_row = 0
        for hcut in hcuts:
            nchips = sum(W[r][c] == '@' for r in range(prev_row, hcut+1)
                         for c in range(prev_col, vcut+1))
            if nchips != chips_per_piece:
                return 'IMPOSSIBLE'
            prev_row = hcut + 1
        prev_col = vcut + 1

    return 'POSSIBLE'


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C, H, V = map(int, input().split())  # rows, columns, horizontal cuts, vertical cuts
        W = [input() for _ in range(R)]  # the waffle matrix

        print('Case #{}: {}'.format(case, check(R, C, H, V, W)))


main()
