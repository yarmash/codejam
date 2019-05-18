#!/usr/bin/env python

"""Alphabet Cake"""

from itertools import product, repeat


def solve_grid(R, C, grid):

    # Try to fill the blank cells vertically with the current initial.
    # If at the end we have blank cells, do the same horizontally.
    for r, c in product(range(R), range(C)):
        i = grid[r][c]
        if i == '?':
            continue

        r1 = r2 = r
        while r1 > 0 and grid[r1-1][c] == '?':
            r1 -= 1
            grid[r1][c] = i
        while r2 < R-1 and grid[r2+1][c] == '?':
            r2 += 1
            grid[r2][c] = i

    if all(grid[r][c] != '?' for r, c in product(range(R), range(C))):
        return

    for r, c in product(range(R), range(C)):
        i = grid[r][c]
        if i == '?':
            continue

        c1 = c2 = c
        while c1 > 0 and grid[r][c1-1] == '?':
            c1 -= 1
            grid[r][c1] = i
        while c2 < C-1 and grid[r][c2+1] == '?':
            c2 += 1
            grid[r][c2] = i


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())
        grid = [list(input()) for _ in repeat(None, R)]

        solve_grid(R, C, grid)

        print(f'Case #{case}:')
        for row in grid:
            print(*row, sep='')


main()
