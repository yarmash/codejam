#!/usr/bin/env python

"""Counting Sheep"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        if N == 0:
            print('Case #{}: INSOMNIA'.format(case))
            continue

        K = str(N)
        digits = set(K)
        i = 1

        while len(digits) != 10:
            i += 1
            K = str(i*N)
            digits.update(K)

        print('Case #{}: {}'.format(case, K))


main()
