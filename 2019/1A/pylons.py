#!/usr/bin/env python

"""Pylons"""

from itertools import product, repeat
from random import shuffle


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())  # the numbers of rows and columns

        def search(moves, grid):
            if len(moves) == R*C:
                return moves

            cells = [(r, c) for r, c in product(range(R), range(C))
                     if (not grid[r][c] and r != moves[-1][0] and c != moves[-1][1]
                         and moves[-1][0] - moves[-1][1] != r - c
                         and moves[-1][0] + moves[-1][1] != r + c)]
            shuffle(cells)
            for r, c in cells:
                g = [r[:] for r in grid]
                g[r][c] = True
                res = search(moves+((r, c),), g)
                if res is not None:
                    return res

        cells = list(product(range(R), range(C)))
        shuffle(cells)

        for r, c in cells:
            grid = [[False]*C for _ in repeat(None, R)]
            grid[r][c] = True
            res = search(((r, c),), grid)
            if res is not None:
                print('Case #{}: POSSIBLE'.format(case))
                for r, c in res:
                    print(r+1, c+1)
                break
        else:
            print('Case #{}: IMPOSSIBLE'.format(case))


main()
