#!/usr/bin/env python

"""Fractiles"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        K, C, S = map(int, input().split())

        print(f'Case #{case}: ', *range(1, K+1))


main()
