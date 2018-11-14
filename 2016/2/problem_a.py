#!/usr/bin/env python

"""Rather Perplexing Showdown"""

from itertools import permutations


def main():
    T = int(input())  # the number of test cases

    winner = {
        ('R', 'S'): 'R',
        ('S', 'R'): 'R',
        ('S', 'P'): 'S',
        ('P', 'S'): 'S',
        ('P', 'R'): 'P',
        ('R', 'P'): 'P',
    }

    def check_perm(N, p):
        that = p

        for _ in range(N):
            this = []
            for x, y in zip(*[iter(that)]*2):
                if x == y:
                    return False
                this.append(winner[(x, y)])
            that = this
        return True

    for case in range(1, T+1):

        N, R, P, S = map(int, input().split())

        lineup = 'P'*P + 'R'*R + 'S'*S

        for p in permutations(lineup):
            if check_perm(N, p):
                print(f'Case #{case}: ', *p, sep='')
                break
        else:
            print(f'Case #{case}: IMPOSSIBLE')


main()
