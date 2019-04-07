#!/usr/bin/env python

"""Steed 2: Cruise Control"""


from collections import namedtuple


Horse = namedtuple('Horse', ('position', 'speed'))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        D, N = map(int, input().split())  # the destination position and the number of other horses on the road

        horses = []

        for _ in range(N):
            K, S = map(int, input().split())  # the initial position and maximum speed of the i-th horse
            horses.append(Horse(K, S))

        tmax = max((D - horse.position) / horse.speed for horse in horses)

        print('Case #{}: {}'.format(case, D / tmax))


main()
