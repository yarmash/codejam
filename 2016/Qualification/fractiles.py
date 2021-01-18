#!/usr/bin/env python3

"""Fractiles"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        K, C, S = map(int, input().split())

        if C*S < K:
            print(f'Case #{case}: IMPOSSIBLE')
            continue

        tiles = []
        for i in range(1, K + 1, C):
            p = 1
            for j in range(C):
                p = (p - 1) * K + min(i + j, K)
            tiles.append(p)

        print(f'Case #{case}:', *tiles)


main()
