#!/usr/bin/env python

"""Cryptopangrams"""

from math import gcd
from string import ascii_uppercase


def main():
    T = int(input())

    for case in range(1, T+1):
        N, L = map(int, input().split())
        values = list(map(int, input().split()))

        primes = [None]*(L+1)

        for i in range(len(values)-1):
            if values[i] != values[i+1]:
                primes[i+1] = gcd(values[i], values[i+1])
                break

        for j in range(i, -1, -1):
            primes[j] = values[j] // primes[j+1]

        for j in range(i+1, len(values)):
            primes[j+1] = values[j] // primes[j]

        chars = dict(zip(sorted(set(primes)), ascii_uppercase))
        plaintext = ''.join(map(chars.get, primes))

        print('Case #{}: {}'.format(case, plaintext))


main()
