#!/usr/bin/env python3

"""Nesting Depth"""


def main():
    T = int(input())

    for case in range(1, T+1):
        S = input()

        S2 = []
        last = 0

        for c in S:
            x = int(c)
            if x > last:
                S2.extend('('*(x-last))
            elif x < last:
                S2.extend(')'*(last-x))
            S2.append(c)
            last = x

        S2.extend(')'*last)

        print('Case #{}: {}'.format(case, ''.join(S2)))


main()
