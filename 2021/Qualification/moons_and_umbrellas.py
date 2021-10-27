#!/usr/bin/env python3

"""Moons and Umbrellas"""

import sys
from functools import lru_cache

sys.setrecursionlimit(5000)  # TODO: get rid of recursion


def main():
    T = int(input())

    for case in range(1, T+1):
        X, Y, S = input().split()
        X = int(X)
        Y = int(Y)
        S = tuple(S)

        @lru_cache(maxsize=128)
        def cost(S):
            if len(S) <= 1:
                return 0

            if S[0] == '?':
                return min(cost(('C',) + S[1:]), cost(('J',) + S[1:]))

            if S[0] in ('C', 'J') and S[1] == '?':
                return min(cost((S[0],) + ('C',) + S[2:]), cost((S[0],) + ('J',) + S[2:]))

            if S[0] == S[1]:
                return cost(S[1:])

            if S[0] == 'C' and S[1] == 'J':
                return X + cost(S[1:])

            if S[0] == 'J' and S[1] == 'C':
                return Y + cost(S[1:])


        print(f'Case #{case}: {cost(S)}')


main()
