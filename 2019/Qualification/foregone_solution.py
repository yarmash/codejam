#!/usr/bin/env python3

"""Foregone Solution"""


def main():
    T = int(input())

    for case in range(1, T+1):
        N = input()
        A = []
        B = []

        for digit in N:
            if digit == '4':
                A.append('3')
                B.append('1')
            else:
                A.append(digit)
                if B:
                    B.append('0')

        print('Case #{}: {} {}'.format(case, ''.join(A), ''.join(B)))


main()
