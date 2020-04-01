#!/usr/bin/env python3

"""Rank and File"""

from collections import Counter


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        cnt = Counter()

        for _ in range(2*N-1):
            cnt.update(int(x) for x in input().split())

        missing = []
        for k, v in sorted(cnt.items()):
            if v & 1:
                missing.append(k)
        missing.sort()

        print(f'Case #{case}: ', *missing)


main()
