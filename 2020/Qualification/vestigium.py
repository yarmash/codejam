#!/usr/bin/env python3

"""Vestigium"""


def trace(M, N):
    return sum(M[i][i] for i in range(N))


def rows(M, N):
    return sum(len(set(r)) != N for r in M)


def cols(M, N):
    return sum(len(set(r[c] for r in M)) != N for c in range(N))


def main():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())  # the size of the matrix
        M = [list(map(int, input().split())) for _ in range(N)]

        print('Case #{}: {} {} {}'.format(case, trace(M, N), rows(M, N), cols(M, N)))


main()
