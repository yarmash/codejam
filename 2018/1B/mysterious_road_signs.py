#!/usr/bin/env python

"""Mysterious Road Signs"""

from collections import Counter


def find_sets(MN, start, stop, sets):
    if start == stop:
        return
    if stop - start == 1 or stop - start == 2:
        sets.add((start, stop))
        return

    midpoint = (start + stop) // 2

    find_sets(MN, start, midpoint, sets)
    find_sets(MN, midpoint+1, stop, sets)

    M = MN[midpoint][0]
    for i in range(midpoint, start-1, -1):
        if MN[i][0] != M:
            break
    N1 = MN[i][1]
    for i in range(midpoint, stop):
        if MN[i][0] != M:
            break
    N2 = MN[i][1]

    N = MN[midpoint][1]
    for i in range(midpoint, start-1, -1):
        if MN[i][1] != N:
            break
    M1 = MN[i][0]
    for i in range(midpoint, stop):
        if MN[i][1] != N:
            break
    M2 = MN[i][0]

    for m, n in ((M, N1), (M, N2), (M1, N), (M2, N)):
        i = midpoint
        while i - 1 >= start and (MN[i-1][0] == m or MN[i-1][1] == n):
            i -= 1

        j = midpoint
        while j + 1 < stop and (MN[j+1][0] == m or MN[j+1][1] == n):
            j += 1

        sets.add((i, j+1))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = int(input())  # the number of road signs

        MN = []
        for _ in range(S):
            D, A, B = map(int, input().split())  # the sign's distance and the numbers on its sides
            MN.append((D + A, D - B))

        sets = set()
        find_sets(MN, 0, len(MN), sets)
        cnt = Counter(x[1] - x[0] for x in sets)
        max_size = max(cnt)

        print('Case #{}: {} {}'.format(case, max_size, cnt[max_size]))


main()
