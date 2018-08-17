#!/usr/bin/env python

"""Bit Party"""

from collections import namedtuple

Cashier = namedtuple('Cashier', ('max_bits', 'scan_time', 'packaging_time'))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, B, C = map(int, input().split())  # robot shoppers, bits, cashiers

        cashiers = []
        max_scan_time = max_packaging_time = 0

        for _ in range(C):
            M, S, P = map(int, input().split())  # max number of bits, scan time per bit, packaging time
            cashier = Cashier(M, S, P)
            cashiers.append(cashier)
            if S > max_scan_time:
                max_scan_time = S
            if P > max_packaging_time:
                max_packaging_time = P

        left, right = 0, max_scan_time*B + max_packaging_time

        while left < right:
            middle = (left + right) // 2

            if sum(sorted((max(0, min(c.max_bits, (middle - c.packaging_time) // c.scan_time)) for c in cashiers),
                          reverse=True)[:R]) < B:
                left = middle + 1
            else:
                right = middle

        print('Case #{}: {}'.format(case, left))


main()
