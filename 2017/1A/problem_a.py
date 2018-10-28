#!/usr/bin/env python

"""Alphabet Cake"""


def main():
    T = int(input())  # the number of test cases

    def print_grid(case, grid):
        print('Case #{}:'.format(case))
        for row in grid:
            print(*row, sep='')

    for case in range(1, T+1):
        R, C = map(int, input().split())
        grid = [list(input()) for _ in range(R)]

        initials = set(grid[r][c] for r in range(R) for c in range(C))

        if '?' not in initials:  # no blank cells
            print_grid(case, grid)
            continue

        if len(initials) == 2:  # a single initial for the grid
            initial = next(i for i in initials if i != '?')
            grid = [[initial]*C]*R
            print_grid(case, grid)
            continue

        # Try to fill the blank cells vertically with the current initial.
        # If at the end we have blank cells, do the same horizontally.
        for r in range(R):
            for c in range(C):
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

        if all(grid[r][c] != '?' for r in range(R) for c in range(C)):
            print_grid(case, grid)
            continue

        for r in range(R):
            for c in range(C):
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

        print_grid(case, grid)


main()
