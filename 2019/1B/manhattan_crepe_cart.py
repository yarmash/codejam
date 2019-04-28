#!/usr/bin/env python

"""Manhattan Crepe Cart"""

from itertools import repeat, product


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        P, Q = map(int, input().split())  # the number of people, and the maximum value of an x or y coordinate

        grid = [[0]*(Q+1) for _ in repeat(None, Q+1)]

        for _ in repeat(None, P):
            X, Y, D = input().split()  # N, S, E, W

            X = int(X)
            Y = int(Y)

            if D == 'N':
                for y in range(Y+1, Q+1):
                    for x in range(Q+1):
                        grid[y][x] += 1
            elif D == 'S':
                for y in range(Y):
                    for x in range(Q+1):
                        grid[y][x] += 1
            elif D == 'E':
                for y in range(Q+1):
                    for x in range(X+1, Q+1):
                        grid[y][x] += 1
            elif D == 'W':
                for y in range(Q+1):
                    for x in range(X):
                        grid[y][x] += 1

        m = max(x for row in grid for x in row)
        x, y = min((x, y) for y, x in product(range(Q+1), repeat=2) if grid[y][x] == m)

        print('Case #{}: {} {}'.format(case, x, y))


main()
