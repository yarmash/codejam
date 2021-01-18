#!/usr/bin/env python3

"""Ample Syrup"""

from heapq import nlargest
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
            print(f'Case #{case}: {area}')
            continue

        pancakes.sort(reverse=True)

        if K == N:
            area = calc_area(pancakes)
            print(f'Case #{case}: {area}')
            continue

        max_area = 0

        for i, p in enumerate(pancakes):
            if i + K > N:
                break
            stack = [p]
            others = nlargest(K-1, pancakes[i+1:], key=lambda x: x[0]*x[1])
            others.sort(reverse=True)  # not strictly necessary, just to follow the statement's rules
            stack.extend(others)
            area = calc_area(stack)
            if area > max_area:
                max_area = area

        print(f'Case #{case}: {max_area}')


main()
