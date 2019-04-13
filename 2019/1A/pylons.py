#!/usr/bin/env python

"""Pylons"""

from itertools import repeat, product


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())  # the numbers of rows and columns

        stack = []

        for r, c in product(range(R), range(C)):
            grid = [[False]*C for _ in repeat(None, R)]
            grid[r][c] = True
            stack.append((((r, c),), grid))

        while stack:
            moves, grid = stack.pop()
            if len(moves) == R*C:
                print('Case #{}: POSSIBLE'.format(case))
                for r, c in moves:
                    print(r+1, c+1)
                break

            for r, c in product(range(R), range(C)):
                if (not grid[r][c] and r != moves[-1][0] and c != moves[-1][1]
                        and moves[-1][0] - moves[-1][1] != r - c
                        and moves[-1][0] + moves[-1][1] != r + c):
                    g = [r.copy() for r in grid]
                    g[r][c] = True
                    stack.append((moves+((r, c),), g))
        else:
            print('Case #{}: IMPOSSIBLE'.format(case))


main()
