#!/usr/bin/env python

"""Pylons"""

from itertools import repeat, product


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())

        grid = [[False]*C for _ in repeat(None, R)]
        stack = []

        for r, c in product(range(R), range(C)):
            g = [row.copy() for row in grid]
            g[r][c] = True
            stack.append((r, c, g, [(r+1, c+1)]))

        """
        r = r'
        c = c'
        r - c = r' - c'
        r + c = r' + c'
        """
        M = R*C

        while stack:
            r, c, g, h = stack.pop()
            if len(h) == M:
                print('Case #{}: POSSIBLE'.format(case))
                for row, col in h:
                    print(row, col)
                break

            for row, col in product(range(R), range(C)):
                if not g[row][col] and row != r and col != c and r - c != row - col and r + c != row + col:
                    g2 = [x.copy() for x in g]
                    g2[row][col] = True
                    stack.append((row, col, g2, h+[(row+1, col+1)]))
        else:
            print('Case #{}: IMPOSSIBLE'.format(case))


main()
