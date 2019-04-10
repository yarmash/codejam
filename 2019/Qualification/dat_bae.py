#!/usr/bin/env python

"""Dat Bae"""

from itertools import repeat
import sys


def main():

    T = int(input())  # the number of test cases

    for i in range(T):
        N, B, F = map(int, input().split())  # the number of workers / broken workers / calls
        workers = [True]*N

        def p(x):
            test = [0]*(x+1) + [1]*(N-x-1)
            assert len(test) == N
            print(*test, sep='', flush=True)
            resp = input()
            if resp == '-1':
                sys.exit()
            return resp.count('0') + b == x+1

        b = left = 0

        for _ in repeat(None, F):
            # use binary search to find the rightmost index for which there're no broken workers
            right = N-1
            while left < right:
                middle = (right + left) // 2

                if p(middle):
                    left = middle + 1
                else:
                    right = middle

            workers[left] = False

            b += 1
            left += 1

            if b == B:
                print(*(i for i, v in enumerate(workers) if not v), flush=True)
                resp = input()
                if resp == '1':
                    break
                if resp == '-1':
                    return
        else:
            return


main()
