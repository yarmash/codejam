#!/usr/bin/env python

"""Dat Bae"""

from itertools import cycle, islice


def main():
    T = int(input())  # the number of test cases

    for i in range(T):
        N, B, F = map(int, input().split())  # the number of workers / broken workers / calls

        F = 5  # enough to solve both test sets

        columns = list(islice(cycle('{:0{width}b}'.format(n, width=F) for n in range(2**F)), N))
        result = ['']*(N-B)

        for i in range(F):
            print(*(c[i] for c in columns), sep='', flush=True)
            resp = input()
            if resp == '-1':
                return
            for i, v in enumerate(resp):
                result[i] += v

        broken_workers = []

        for i, v in enumerate(columns):
            if len(result) == i or result[i] != v:
                result.insert(i, v)
                broken_workers.append(i)

        print(*broken_workers, flush=True)
        resp = input()
        if resp != '1':
            return


main()
