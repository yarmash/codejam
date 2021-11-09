#!/usr/bin/env python3

"""Mushroom Monster"""


def method1(N, m):
    res = 0
    for i in range(1, N):
        if m[i] < m[i-1]:
            res += m[i-1] - m[i]
    return res


def method2(N, m):
    res = min_rate = 0

    for i in range(1, N):
        if m[i-1] - m[i] > min_rate:
            min_rate = m[i-1] - m[i]

    for i in range(1, N):
        res += min(min_rate, m[i-1])
    return res


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        m = [int(x) for x in input().split()]

        x = method1(N, m)
        y = method2(N, m)

        print(f'Case #{case}: {x} {y}')


main()
