#!/usr/bin/env python3

"""Alien Rhyme"""

from itertools import repeat
from collections import Counter


# TODO: implement the solution using a trie (as described in the analysis)
def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        cnt = Counter(input().rjust(50) for _ in repeat(None, N))
        words = 0

        for _ in repeat(None, 50):
            for k, v in cnt.items():
                if v >= 2:
                    cnt[k] -= 2
                    words += 2
            cnt = Counter(e[1:] for e in cnt.elements())

        print('Case #{}: {}'.format(case, words))


main()
