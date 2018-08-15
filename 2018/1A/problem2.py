#!/usr/bin/env python

"""Bit Party"""

from itertools import chain, combinations, combinations_with_replacement


class Cashier:
    __slots__ = ('max_bits', 'scan_time', 'packaging_time')

    def __init__(self, M, S, P):
        self.max_bits = M
        self.scan_time = S
        self.packaging_time = P


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, B, C = map(int, input().split())  # robot shoppers, bits, cashiers

        cashiers = []

        for _ in range(C):
            M, S, P = map(int, input().split())  # max number of bits, scan time per bit, packaging time
            cashier = Cashier(M, S, P)
            cashiers.append(cashier)

        res = float('inf')

        for num_cashiers in range(1, R+1):
            for sel_cashiers in combinations(cashiers, num_cashiers):
                for bits_bars in combinations_with_replacement(range(B+1), num_cashiers-1):
                    prev_bar = 0
                    times = []

                    for cashier, bar in zip(sel_cashiers, chain(bits_bars, (B,))):
                        num_bits = bar - prev_bar
                        prev_bar = bar
                        if num_bits > cashier.max_bits:
                            break
                        times.append(num_bits*cashier.scan_time + cashier.packaging_time)
                    else:
                        time = max(times)
                        if time < res:
                            res = time

        print('Case #{}: {}'.format(case, res))


main()
