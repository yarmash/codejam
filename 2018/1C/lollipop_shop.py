#!/usr/bin/env python

"""Lollipop Shop"""


def main():
    T = int(input())  # the number of test cases

    for _ in range(T):
        N = int(input())  # the number of lollipops/customers
        F = set(range(N))  # available flavors

        freq = [0]*N

        for _ in range(N):
            D, *P = map(int, input().split())  # number of flavors, preferences

            if D == 0:
                print(-1, flush=True)
                continue

            for p in P:
                freq[p] += 1

            for x in sorted(P, key=freq.__getitem__):
                if x in F:
                    print(x, flush=True)
                    F.remove(x)
                    break
            else:
                print(-1, flush=True)


main()
