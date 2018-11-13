#!/usr/bin/env python

"""Senate Evacuation"""

import string
from heapq import heappop, heappush


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())  # the number of parties
        *P, = map(int, input().split())
        h = []

        for party, senators in zip(string.ascii_uppercase, P):
            heappush(h, (-senators, party))

        res = []

        while h:
            if len(h) == 2:
                pair = []
                for _ in range(2):
                    senators, party = heappop(h)
                    pair.append(party)
                    senators += 1
                    if senators < 0:
                        heappush(h, (senators, party))
                res.append(''.join(pair))
            else:
                senators, party = heappop(h)
                res.append(party)
                senators += 1

                if senators < 0:
                    heappush(h, (senators, party))

        print(f'Case #{case}: {" ".join(res)}')


main()
