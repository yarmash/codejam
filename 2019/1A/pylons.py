#!/usr/bin/env python

"""Pylons"""

# TODO: implement the solution using the 'constructive' approach mentioned in the analysis

import random
from itertools import product, repeat


def select_random_element(it, randrange=random.randrange):
    """
    Return a random element from iterator (exhausting the iterator).
    If the iterator is empty, return `None`.
    The algorithm runs in O(n) time and O(1) space.
    """
    selection = None
    for i, item in enumerate(it, start=1):
        if randrange(i) == 0:  # random int in range [0..i)
            selection = item
    return selection


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())  # the numbers of rows and columns

        if R < 2 or C < 2 or R + C < 7:
            print('Case #{}: IMPOSSIBLE'.format(case))
        else:
            print('Case #{}: POSSIBLE'.format(case))

            while True:
                grid = [[False]*C for _ in repeat(None, R)]
                moves = []
                last = None
                for _ in repeat(None, R*C):
                    it = (product(range(R), range(C)) if last is None
                          else
                          ((r, c) for r, c in product(range(R), range(C)) if not grid[r][c]
                           and r != last[0] and c != last[1] and last[0] - last[1] != r - c
                           and last[0] + last[1] != r + c))
                    cell = select_random_element(it)
                    if cell is None:
                        break
                    moves.append(cell)
                    grid[cell[0]][cell[1]] = True
                    last = cell
                else:
                    for r, c in moves:
                        print(r+1, c+1)
                    break


main()
