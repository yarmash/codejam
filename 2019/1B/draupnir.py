#!/usr/bin/env python3

"""Draupnir"""

from itertools import repeat


def main():
    T, W = map(int, input().split())

    for _ in repeat(None, T):
        a = b = c = d = e = f = 0
        # the total number of rings on day i
        # a*2^i + b*2^(i//2) + c*2^(i//3) + d*2^(i//4) + e*2^(i//5) + f*2(i//6)

        # TODO: determine appropriate values for days dynamically
        print(200, flush=True)
        rings = int(input())  # a*2^200 + b*2^100 + c*2^66 + d*2^50 + e*2^40 + f*2^33

        f = (rings % 2**40) // 2**33
        e = ((rings - f*2**33) % 2**50) // 2**40
        d = (rings - f*2**33 - e*2**40) // 2**50

        print(56, flush=True)
        rings = int(input())  # a*2*56 + b*2^28 + c*2^18 + d*2^14 + e*2^11 + f*2^9

        c = ((rings - f*2**9 - e*2**11 - d*2**14) % 2**28) // 2**18
        b = ((rings - f*2**9 - e*2**11 - d*2**14 - c*2**18) % 2**56) // 2**28
        a = (rings - f*2**9 - e*2**11 - d*2**14 - c*2**18 - b*2**28) // 2**56

        print(a, b, c, d, e, f)

        if input() == '-1':
            return


main()
