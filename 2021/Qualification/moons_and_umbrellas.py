#!/usr/bin/env python3

"""Moons and Umbrellas"""

from collections import Counter


def choose(pic, S, i, X, Y):
    cost = 0
    if pic == 'J':
        if i > 0 and S[i-1] == 'C':
            cost += X
        if i < len(S)-1 and S[i+1] == 'C':
            cost += Y
    else:
        if i > 0 and S[i-1] == 'J':
            cost += Y
        if i < len(S)-1 and S[i+1] == 'J':
            cost += X
    return cost


def main():
    T = int(input())

    for case in range(1, T+1):
        X, Y, S = input().split()
        X = int(X)
        Y = int(Y)
        print(X, Y, S)

        S = list(S)

        if S[0] == '?':
            for i in range(1, len(S)):
                if S[i] != '?':
                    break

            for j in range(i-1, -1, -1):
                cost1 = choose('J', S, j, X, Y)
                cost2 = choose('C', S, j, X, Y)
                print(j, cost1, cost2, S)

                if cost1 < cost2:
                    S[j] = 'J'
                elif cost2 < cost1:
                    S[j] = 'C'
                else:
                    S[j] = 'J'
        print(S)

        for i in range(len(S)):
            if S[i] == '?':
                cost1 = choose('J', S, i, X, Y)
                cost2 = choose('C', S, i, X, Y)
                if cost1 < cost2:
                    S[i] = 'J'
                elif cost2 < cost1:
                    S[i] = 'C'
                else:
                    S[i] = 'J'

        S = ''.join(S)
        cost = X*S.count('CJ') + Y * S.count('JC')

        print(f'Case #{case}: {cost}')


main()
