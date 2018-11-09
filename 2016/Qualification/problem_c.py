#!/usr/bin/env python

"""Coin Jam"""


from itertools import product


def main():
    T = int(input())  # the number of test cases

    digits = '01'

    for case in range(1, T+1):
        N, J = map(int, input().split())
        print('Case #{}:'.format(case))

        jamcoins = 0

        for p in product(digits, repeat=N-2):
            n = f'1{"".join(p)}1'

            divisors = []

            for base in range(2, 11):
                k = int(n, base=base)
                for d in range(2, 10):
                    if k % d == 0:
                        divisors.append(d)
                        break
                else:
                    break
            else:
                jamcoins += 1
                print(n, *divisors)
                if jamcoins == J:
                    break


main()
