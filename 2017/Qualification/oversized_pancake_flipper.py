#!/usr/bin/env python3

"""Oversized Pancake Flipper"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S, K = input().split()
        K = int(K)
        L = list(S)

        i = 0
        times = 0

        while True:
            try:
                i = L.index('-', i)
            except ValueError:
                i = -1

            if i == -1 or i + K > len(L):
                break

            for j in range(i, i+K):
                L[j] = '+' if L[j] == '-' else '-'
            times += 1

        if i == -1:
            print(f'Case #{case}: {times}')
        else:
            print(f'Case #{case}: IMPOSSIBLE')


main()
