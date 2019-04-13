#!/usr/bin/env python

"""Alien Rhyme"""

from itertools import combinations, repeat, permutations, takewhile


def common_prefix(i1, i2):
    return ''.join(x[0] for x in takewhile(lambda x: x[0] == x[1], zip(reversed(i1), reversed(i2))))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())
        words = [input() for _ in repeat(None, N)]

        max_pairs = 0

        for p in permutations(words):
            pairs = 0
            seen = set()
            seenpr = set()

            for c in combinations(p, 2):
                if c[0] in seen or c[1] in seen:
                    continue
                seen.add(c[0])
                seen.add(c[1])

                pr = common_prefix(*c)
                if pr and pr not in seenpr:
                    pairs += 1
                    seenpr.add(pr)

            if pairs > max_pairs:
                max_pairs = pairs

        print('Case #{}: {}'.format(case, max_pairs*2))


main()
