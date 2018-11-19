#!/usr/bin/env python

"""Rather Perplexing Showdown"""


def main():
    T = int(input())  # the number of test cases

    match = {
        'P': ('P', 'R'),
        'R': ('R', 'S'),
        'S': ('P', 'S'),
    }

    lineups = {}

    for winner in ('P', 'R', 'S'):
        prev_round = [winner]

        for n in range(1, 13):  # 1 ≤ N ≤ 12
            this_round = [y for x in prev_round for y in match[x]]
            key = (this_round.count('P'), this_round.count('R'), this_round.count('S'))
            lineups.setdefault(n, {})[key] = this_round
            prev_round = this_round

    for case in range(1, T+1):
        N, R, P, S = map(int, input().split())

        lineup = lineups[N].get((P, R, S))

        if lineup is None:
            print(f'Case #{case}: IMPOSSIBLE')
        else:
            # find the alphabetically earliest version of the lineup
            chunk_size = 4
            while chunk_size <= len(lineup):
                for i in range(0, len(lineup)-chunk_size+1, chunk_size):
                    left, right = lineup[i:i+chunk_size//2], lineup[i+chunk_size//2:i+chunk_size]
                    if left > right:
                        lineup[i:i+chunk_size] = right + left
                chunk_size *= 2

            print(f'Case #{case}: ', *lineup, sep='')


main()
