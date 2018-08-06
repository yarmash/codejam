#!/usr/bin/env python

"""A Whole New Word"""

from itertools import product


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, L = map(int, input().split())  # the number of words and the length

        words = set()
        letters = [set() for _ in range(L)]

        for _ in range(N):
            word = input()
            words.add(word)
            for i, l in enumerate(word):
                letters[i].add(l)

        if L == 1:
            print('Case #{}: {}'.format(case, '-'))
            continue

        for p in product(*letters):
            if ''.join(p) not in words:
                print('Case #{}: {}'.format(case, ''.join(p)))
                break
        else:
            print('Case #{}: {}'.format(case, '-'))

main()
