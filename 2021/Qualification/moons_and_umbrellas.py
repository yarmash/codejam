#!/usr/bin/env python3

"""Moons and Umbrellas"""


INF = float('inf')


def solve_case(case):
    X, Y, S = input().split()
    X = int(X)  # CJ
    Y = int(Y)  # JC

    dp = {'C': 0, 'J': INF} if S[0] == 'C' else {'C': INF, 'J': 0} if S[0] == 'J' else {'C': 0, 'J': 0}

    for i, c in enumerate(S[1:], 1):
        if c == 'C':
            if S[i-1] == 'C':
                dp = {'C': dp['C'], 'J': INF}
            elif S[i-1] == 'J':
                dp = {'C': dp['J'] + Y, 'J': INF}
            else:
                dp = {'C': min(dp['C'], dp['J'] + Y), 'J': INF}
        elif c == 'J':
            if S[i-1] == 'C':
                dp = {'C': INF, 'J': dp['C'] + X}
            elif S[i-1] == 'J':
                dp = {'C': INF, 'J': dp['J']}
            else:
                dp = {'C': INF, 'J': min(dp['J'], dp['C'] + X)}
        else:
            if S[i-1] == 'C':
                dp = {'C': dp['C'], 'J': dp['C'] + X}
            elif S[i-1] == 'J':
                dp = {'C': dp['J'] + Y, 'J': dp['J']}
            else:
                dp = {'C': min(dp['C'], dp['J'] + Y), 'J': min(dp['J'], dp['C'] + X)}

    print(f'Case #{case}: {min(dp.values())}')


def main():
    T = int(input())

    for case in range(1, T+1):
        solve_case(case)


main()
