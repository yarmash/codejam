#!/usr/bin/env python

"""Golf Gophers"""

from itertools import repeat
from collections import defaultdict


def main():
    T, N, M = map(int, input().split())

    for _ in repeat(None, T):
        seen = defaultdict(int)

        for n in range(N):
            print(*[18]*18, flush=True)

            resp = input()
            if resp == '-1':
                return

            m = sum(map(int, resp.split()))
            seen[m] += 1

        print(max(seen, key=seen.get), flush=True)

        resp = input()
        if resp != '1':
            return


main()
