#!/usr/bin/env python3

"""Reversort"""


def main():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())  # the number of elements in the input list
        L = [int(x) for x in input().split()]

        cost = 0

        for i in range(N-1):
            j = min(range(i, N), key=L.__getitem__)
            L[i:j+1] = L[j-N:i-N-1:-1]
            cost += j - i + 1

        print(f'Case #{case}: {cost}')


main()
