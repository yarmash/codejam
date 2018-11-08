#!/usr/bin/env python

"""Revenge of the Pancakes"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = input()  # the stack
        grouped_height = 1 + S.count('-+') + S.count('+-')
        flips = grouped_height if S.endswith('-') else grouped_height - 1
        print('Case #{}: {}'.format(case, flips))


main()
