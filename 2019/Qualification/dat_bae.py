#!/usr/bin/env python

"""Dat Bae"""


def main():
    T = int(input())  # the number of test cases

    for i in range(T):
        N, B, F = map(int, input().split())  # the number of workers / broken workers / calls

        columns = ['{:0{width}b}'.format(n, width=F) for n in range(N)]
        result = ['']*(N-B)

        for i in range(F):
            print(*(c[i] for c in columns), sep='', flush=True)
            resp = input()
            if resp == '-1':
                return
            for i, v in enumerate(resp):
                result[i] += v

        received_columns = set(result)
        print(*(i for i, c in enumerate(columns) if c not in received_columns), flush=True)
        resp = input()
        if resp == '-1':
            return


main()
