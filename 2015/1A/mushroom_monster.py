#!/usr/bin/env python3

"""Mushroom Monster"""


def method1(N, m):
    return sum(m[i-1] - m[i] for i in range(1, N) if m[i] < m[i-1])


def method2(N, m):
    rate = max(m[i-1] - m[i] for i in range(1, N))
    return sum(min(rate, m[i-1]) for i in range(1, N))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        m = [int(x) for x in input().split()]

        x = method1(N, m)
        y = method2(N, m)

        print(f'Case #{case}: {x} {y}')


main()
