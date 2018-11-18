#!/usr/bin/env python

"""Rather Perplexing Showdown"""

from collections import Counter


def main():
    T = int(input())  # the number of test cases

    match = {
        'P': ('P', 'R'),
        'R': ('R', 'S'),
        'S': ('P', 'S'),
    }

    lineups = {}

    for winner in ('P', 'R', 'S'):
        tree = [winner]

        for n in range(1, 13):  # 1 ≤ N ≤ 12
            r = []
            for w in tree[-1]:
                r.extend(match[w])
            tree.append(r)

            cnt = Counter(r)
            key = (cnt.get('P', 0), cnt.get('R', 0), cnt.get('S', 0))
            lineups.setdefault(n, {})[key] = r

    for case in range(1, T+1):
        N, R, P, S = map(int, input().split())

        lineup = lineups[N].get((P, R, S))

        if lineup is None:
            print(f'Case #{case}: IMPOSSIBLE')
        else:
            # find the alphabetically earliest lineup
            chunk_size = 4
            while chunk_size <= len(lineup):
                for i in range(0, len(lineup)-chunk_size+1, chunk_size):
                    if lineup[i:i+chunk_size//2] > lineup[i+chunk_size//2:i+chunk_size]:
                        lineup[i:i+chunk_size//2], lineup[i+chunk_size//2:i+chunk_size] = lineup[i+chunk_size//2:i+chunk_size], lineup[i:i+chunk_size//2]
                chunk_size *= 2

            print(f'Case #{case}: ', *lineup, sep='')


main()
