#!/usr/bin/env python

"""Draupnir"""

from itertools import repeat


def main():
    T, W = map(int, input().split())

    for _ in repeat(None, T):
        a = b = c = d = e = f = 0
        # the total number of rings on day i
        # a*2^i + b*2^(i//2) + c*2^(i//3) + d*2^(i//4) + e*2^(i//5) + f*2(i//6)

        print(5*63, flush=True)  # f*2^52
        f = int(input()) // 2**52

        print(4*63, flush=True)  # e*2^50 + f*2^42
        e = (int(input()) - f*2**42) // 2**50

        print(3*63, flush=True)  # d*2^47 + e*2^37 + f*2^31
        d = (int(input()) - f*2**31 - e*2**37) // 2**47

        print(2*63, flush=True)  # c*2**42 + d*2**31 + e*2**25 + f*2**21
        c = (int(input()) - d*2**31 - e*2**25 - f*2**21) // 2**42

        print(63, flush=True)  # b*2**31 + c*2**21 + d*2**15 + e*2**12 + f*2**10
        b = (int(input()) - c*2**21 - d*2**15 - e*2**12 - f*2**10) // 2**31

        print(1, flush=True)  # a*2 + b + c + d + e + f
        a = (int(input()) - b - c - d - e - f) // 2

        print(a, b, c, d, e, f)

        if input() == '-1':
            return


main()
