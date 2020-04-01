#!/usr/bin/env python3

"""Trouble Sort"""

from collections import Counter


def main():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())
        L = list(map(int, input().split()))

        c1 = Counter(L[::2])
        c2 = Counter(L[1::2])

        L.sort()
        valid = 0

        for i, v in enumerate(L):
            if i % 2 == 0:
                if c1[v]:
                    valid += 1
                    c1[v] -= 1
                else:
                    break
            else:
                if c2[v]:
                    valid += 1
                    c2[v] -= 1
                else:
                    break
        if valid == N:
            valid = 'OK'

        print('Case #{}: {}'.format(case, valid))


main()
