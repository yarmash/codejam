#!/usr/bin/env python3

"""Moons and Umbrellas"""


def main():
    T = int(input())

    for case in range(1, T+1):
        X, Y, S = input().split()
        X = int(X)
        Y = int(Y)
        S = list(S)

        if S[0] == '?':
            for i in range(1, len(S)):
                if S[i] != '?':
                    S[:i] = [S[i]]*i
                    break
            else:
                S[:] = ['J']*len(S)

        for i in range(1, len(S)):
            if S[i] == '?':
                S[i] = S[i-1]

        S = ''.join(S)
        cost = X * S.count('CJ') + Y * S.count('JC')

        print(f'Case #{case}: {cost}')


main()
