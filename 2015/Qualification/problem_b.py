#!/usr/bin/env python

"""Infinite House of Pancakes"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        input()  # the number of diners with non-empty plates, ignored
        diners = list(map(int, input().split()))

        minutes = float('inf')
        stack = [(diners.copy(), 0)]

        while stack:
            d, m = stack.pop()
            md = max(d)
            if m + md < minutes:
                minutes = m + md

            # split the largest plate
            if m < minutes:
                half = md // 2
                for i in range(1, half+1):
                    t = d.copy()
                    j = t.index(md)
                    t[j] -= i
                    t.append(i)
                    stack.append((t, m+1))


        print(f'Case #{case}: {minutes}')


main()
