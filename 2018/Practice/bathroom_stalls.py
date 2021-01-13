#!/usr/bin/env python3

"""Bathroom Stalls"""

from collections import defaultdict


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):

        N, K = map(int, input().split())
        S = {N}
        count = defaultdict(int)
        count[N] = 1
        P = 0

        while True:
            chunk = max(S)

            if chunk & 1:
                min_s = max_s = chunk // 2
            else:
                max_s = chunk // 2
                min_s = max_s - 1

            P += count[chunk]

            if P >= K:
                break

            S.remove(chunk)
            S.add(min_s)
            S.add(max_s)

            count[max_s] += count[chunk]
            count[min_s] += count[chunk]

        print(f'Case #{case}: {max_s} {min_s}')


main()
