#!/usr/bin/env python

"""Mysterious Road Signs"""

from collections import defaultdict


def is_valid_set(NM, start, stop):
    if stop-start == 1:
        return True

    M = NM[start][0]
    for i in range(start+1, stop):
        if NM[i][0] != M:
            break
    else:
        return True
    N = NM[i][1]
    for j in range(i+1, stop):
        if NM[j][0] != M and NM[j][1] != N:
            break
    else:
        return True

    N = NM[start][1]
    for i in range(start+1, stop):
        if NM[i][1] != N:
            break
    else:
        return True
    M = NM[i][0]
    for j in range(i+1, stop):
        if NM[j][0] != M and NM[j][1] != N:
            return False
    return True


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = int(input())  # the number of road signs

        NM = []
        for _ in range(S):
            D, A, B = map(int, input().split())  # the sign's distance and the numbers on its sides
            NM.append((D + A, D - B))

        cnt = defaultdict(int)
        max_size = 0

        for i in range(len(NM)):
            if len(NM) - i < max_size:
                break
            for j in range(i+1, len(NM)+1):
                if is_valid_set(NM, i, j):
                    size = j - i
                    cnt[size] += 1
                    if size > max_size:
                        max_size = size
                else:
                    break

        print('Case #{}: {} {}'.format(case, max_size, cnt[max_size]))


main()
