#!/usr/bin/env python

"""Tidy Numbers"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = input()
        L = list(map(int, N))

        i = 0
        while i < len(L)-1 and L[i] <= L[i+1]:
            i += 1

        if i == len(L) - 1:
            print('Case #{}: {}'.format(case, N))
        else:
            L[i] -= 1
            while i > 0 and L[i] < L[i-1]:
                i -= 1
                L[i] -= 1
            L[i+1:] = [9]*(len(L)-i-1)

            print('Case #{}: {}'.format(case, int(''.join(map(str, L)))))


main()
