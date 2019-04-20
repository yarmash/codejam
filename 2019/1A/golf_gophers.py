#!/usr/bin/env python

"""Golf Gophers"""

from functools import reduce
from itertools import repeat
from operator import mul


def chinese_remainder(n, a):
    """
    Chinese Remainder Theorem.

    :param n: list of pairwise relatively prime integers
    :param a: remainders when x is divided by n
    """
    s = 0
    prod = reduce(mul, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * inverse(p, n_i) * p
    return s % prod


def inverse(a, b):
    """
    Modular multiplicative inverse.
    """
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    T, N, M = map(int, input().split())

    numbers = (7, 11, 13, 15, 16, 17)  # pairwise coprime

    for _ in repeat(None, T):
        remainders = []
        for n in numbers:
            print(*[n]*18, flush=True)

            resp = input()
            if resp == '-1':
                return

            r = sum(map(int, resp.split())) % n
            remainders.append(r)

        print(chinese_remainder(numbers, remainders), flush=True)

        resp = input()
        if resp != '1':
            return


main()
