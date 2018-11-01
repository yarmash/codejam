#!/usr/bin/env python

"""Ample Syrup"""

from itertools import combinations
from math import pi


def main():
    def calc_area(pancakes):
        area = pi*(pancakes[0][0]**2)
        for p in pancakes:
            area += 2*pi*p[0]*p[1]

        return area

    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, K = map(int, input().split())  # total number of pancakes and the size of the stack

        pancakes = []

        for _ in range(N):
            R, H = map(int, input().split())  # the radius and height of the i-th pancake
            pancakes.append((R, H))

        if K == 1:
            area = max(calc_area([p]) for p in pancakes)
            print('Case #{}: {}'.format(case, area))
            continue

        pancakes.sort(reverse=True)

        if K == N:
            area = calc_area(pancakes)
            print('Case #{}: {}'.format(case, area))
            continue

        # remove needed number of pancakes
        indices = list(range(N))
        max_area = 0

        for c in combinations(indices, N-K):
            area = calc_area([v for i, v in enumerate(pancakes) if i not in c])
            if area > max_area:
                max_area = area

        print('Case #{}: {}'.format(case, max_area))


main()
