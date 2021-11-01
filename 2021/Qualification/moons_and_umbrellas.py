#!/usr/bin/env python3

"""Moons and Umbrellas"""


INF = float('inf')


def solve_case(case):
    X, Y, S = input().split()
    X = int(X)  # CJ
    Y = int(Y)  # JC

    dp = [None]*len(S)
    dp[0] = {'C': 0, 'J': INF} if S[0] == 'C' else {'C': INF, 'J': 0} if S[0] == 'J' else {'C': 0, 'J': 0}

    for i, c in enumerate(S[1:], 1):
        if c == 'C':
            if S[i-1] == 'C':
                dp[i] = {'C': dp[i-1]['C'], 'J': INF}
            elif S[i-1] == 'J':
                dp[i] = {'C': dp[i-1]['J'] + Y, 'J': INF}
            else:
                dp[i] = {'C': min(dp[i-1]['C'], dp[i-1]['J'] + Y), 'J': INF}
        elif c == 'J':
            if S[i-1] == 'C':
                dp[i] = {'C': INF, 'J': dp[i-1]['C'] + X}
            elif S[i-1] == 'J':
                dp[i] = {'C': INF, 'J': dp[i-1]['J']}
            else:
                dp[i] = {'C': INF, 'J': min(dp[i-1]['J'], dp[i-1]['C'] + X)}
        else:
            if S[i-1] == 'C':
                dp[i] = {'C': dp[i-1]['C'], 'J': dp[i-1]['C'] + X}
            elif S[i-1] == 'J':
                dp[i] = {'C': dp[i-1]['J'] + Y, 'J': dp[i-1]['J']}
            else:
                dp[i] = {'C': min(dp[i-1]['C'], dp[i-1]['J'] + Y), 'J': min(dp[i-1]['J'], dp[i-1]['C'] + X)}

    print(f'Case #{case}: {min(dp[-1].values())}')


def main():
    T = int(input())

    for case in range(1, T+1):
        solve_case(case)


main()
