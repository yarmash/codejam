#!/usr/bin/env python

"""Infinite House of Pancakes"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        D = int(input())  # the number of diners with non-empty plates
        diners = list(map(int, input().split()))

        minutes = max(diners)  # the max stack of pancakes (= the max time)

        # try to arrange all pancakes to stacks of equal height
        for ncakes in range(1, minutes):
            s = sum([(d - 1) // ncakes for d in diners if d > ncakes])  # number of special minutes
            if s + ncakes < minutes:
                minutes = s + ncakes

        print(f'Case #{case}: {minutes}')


main()
