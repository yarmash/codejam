#!/usr/bin/env python

"""Bathroom Stalls"""

from heapq import heappop, heappush


def main():
    def get_subchunks(chunk):
        if chunk & 1:
            if chunk == 1:
                mins = maxs = 0
            else:
                mins = maxs = chunk // 2
        else:
            maxs = chunk // 2
            mins = maxs - 1
        return maxs, mins

    T = int(input())  # the number of test cases

    for case in range(1, T+1):

        N, K = map(int, input().split())

        h = [-N]

        for _ in range(K):
            chunk = -heappop(h)
            maxs, mins = get_subchunks(chunk)
            heappush(h, -mins)
            heappush(h, -maxs)

        print('Case #{}: {} {}'.format(case, maxs, mins))


main()
