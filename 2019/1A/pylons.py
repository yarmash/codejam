#!/usr/bin/env python

"""Pylons"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())  # the numbers of rows and columns

        if R < 2 or C < 2 or R + C < 7:
            print('Case #{}: IMPOSSIBLE'.format(case))
        else:
            print('Case #{}: POSSIBLE'.format(case))

            if R > C:
                R, C = C, R
                swapped = True
            else:
                swapped = False

            if R == C == 4:  # this has to be special-cased
                moves = ((1, 1), (2, 3), (3, 1), (4, 3), (1, 2), (2, 4), (3, 2), (4, 4),
                         (1, 3), (2, 1), (3, 3), (4, 1), (3, 4), (4, 2), (1, 4), (2, 2))
            else:
                moves = []
                rows = 0  # processed rows
                while rows != R:
                    if rows + 3 == R:  # insert a 3-row pattern
                        for c in range(C):
                            moves.extend(((rows + 1, c + 1),
                                          (rows + 2, (c + 2) % C + 1),
                                          (rows + 3, c + 1)))
                        rows += 3
                    else:  # insert a 2-row pattern
                        for c in range(C):
                            moves.extend(((rows + 1, (c + 2) % C + 1),
                                          (rows + 2, c + 1)))
                        rows += 2

            for r, c in moves:
                if swapped:
                    r, c = c, r
                print(r, c)


main()
