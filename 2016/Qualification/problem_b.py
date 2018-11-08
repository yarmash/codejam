#!/usr/bin/env python

"""Revenge of the Pancakes"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = list(input())  # the stack

        while S and S[-1] == '+':
            S.pop()

        flips = 0

        while S:
            if S[0] == '-':
                S = ['-' if x == '+' else '+' for x in reversed(S)]
                while S and S[-1] == '+':
                    S.pop()
            else:
                i = 0
                while S[i] == '+':
                    i += 1

                S[:i] = ['-' if x == '+' else '+' for x in S[i-1:-1:-1]]

            flips += 1

        print('Case #{}: {}'.format(case, flips))


main()
