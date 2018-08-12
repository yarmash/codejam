#!/usr/bin/env python

"""Bit Party"""


def search(avail_cashiers, chosen_cashiers, B, R):
    if B == 0:
        yield max(k[1]*v + k[2] for k, v in chosen_cashiers.items())
    else:
        if R > 0:
            for c in avail_cashiers:
                bits = min(B, c[0])

                for b in range(1, bits+1):
                    avail = [cashier for cashier in avail_cashiers if cashier != c]
                    chosen = chosen_cashiers.copy()
                    chosen[c] = b

                    yield from search(avail, chosen, B-b, R-1)


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, B, C = map(int, input().split())  # robot shoppers, bits, cashiers

        cashiers = []

        for _ in range(C):
            M, S, P = map(int, input().split())  # max number of bits, scan time per bit, packaging time
            cashiers.append((M, S, P))

        time = min(search(cashiers, {}, B, R))

        print('Case #{}: {}'.format(case, time))


main()
