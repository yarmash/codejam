#!/usr/bin/env python

"""Bathroom Stalls"""

from collections import defaultdict
from heapq import heappop, heappush


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, K = map(int, input().split())
        h = [-N]
        cnt = defaultdict(int)
        cnt[N] += 1

        for _ in range(K):
            chunk = -h[0]
            cnt[chunk] -= 1

            if not cnt[chunk]:
                heappop(h)

            if chunk & 1:
                if chunk == 1:
                    min_s = max_s = 0
                else:
                    min_s = max_s = chunk // 2
                    if not cnt[min_s]:
                        heappush(h, -min_s)

                    cnt[min_s] += 2
            else:
                max_s = chunk // 2
                min_s = max_s - 1

                if min_s and not cnt[min_s]:
                    heappush(h, -min_s)
                if not cnt[max_s]:
                    heappush(h, -max_s)

                cnt[min_s] += 1
                cnt[max_s] += 1

        print('Case #{}: {} {}'.format(case, max_s, min_s))


main()
