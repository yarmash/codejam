#!/usr/bin/env python

"""Revenge of the Pancakes"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = input()  # the stack
        grouped_height = 1 + S.count('-+') + S.count('+-')
        flips = grouped_height if S[-1] == '-' else grouped_height - 1
        print(f'Case #{case}: {flips}')


main()
