#!/usr/bin/env python3

"""Moons and Umbrellas"""


def main():
    T = int(input())

    for case in range(1, T+1):
        X, Y, S = input().split()
        X = int(X)
        Y = int(Y)
        S = list(S)

        S = ''.join(S).replace('?', '')

        cost = X * S.count('CJ') + Y * S.count('JC')

        print(f'Case #{case}: {cost}')


main()
