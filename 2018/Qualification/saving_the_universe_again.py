#!/usr/bin/env python3

"""Saving The Universe Again"""


def calc_damage(s):
    damage = 0
    strength = 1

    for x in s:
        if x == 'S':
            damage += strength
        else:
            strength *= 2

    return damage


def swap_one(L):
    for i in range(len(L)-2, -1, -1):
        if L[i] == 'C' and L[i+1] == 'S':
            L[i], L[i+1] = L[i+1], L[i]
            return True
    return False


def calc_hacks(D, P):
    d = calc_damage(P)
    if d == 0:
        return 0

    h = 0

    if d > D:
        if 'C' not in P:
            return 'IMPOSSIBLE'

        L = list(P)
        while swap_one(L):
            h += 1
            d = calc_damage(L)
            if d <= D:
                return h

        return 'IMPOSSIBLE'

    return h


def main():
    T = int(input())

    for case in range(1, T+1):
        D, P = input().split()
        D = int(D)
        h = calc_hacks(D, P)
        print('Case #{}: {}'.format(case, h))


main()
