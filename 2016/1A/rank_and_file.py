#!/usr/bin/env python3

"""Rank and File"""

from collections import Counter


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())  # the size of the grid
        cnt = Counter(int(x) for _ in range(2*N-1) for x in input().split())

        missing = [k for k, v in cnt.items() if v & 1]
        missing.sort()

        print(f'Case #{case}: ', *missing)


main()
