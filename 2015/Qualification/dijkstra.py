#!/usr/bin/env python3

"""Dijkstra"""

mul_map = {
    1: {
        'i': 'i',
        'j': 'j',
        'k': 'k',
    },
    -1: {
        'i': '-i',
        'j': '-j',
        'k': '-k',
    },
    'i': {
        'i': -1,
        'j': 'k',
        'k': '-j',
    },
    '-i': {
        'i': 1,
        'j': '-k',
        'k': 'j',
    },
    'j': {
        'i': '-k',
        'j': -1,
        'k': 'i',
    },
    '-j': {
        'i': 'k',
        'j': 1,
        'k': '-i',
    },
    'k': {
        'i': 'j',
        'j': '-i',
        'k': -1,
    },
    '-k': {
        'i': '-j',
        'j': 'i',
        'k': 1,
    },
}


def check_string(S):
    x = 1
    for i in range(len(S) - 2):
        x = mul_map[x][S[i]]
        if x == 'i':
            y = 1
            for j in range(i+1, len(S) - 1):
                y = mul_map[y][S[j]]
                if y == 'j':
                    return True
    return False


def multiply(C, X):
    res = 1
    for _ in range(X % 4):
        for val in C:
            res = mul_map[res][val]
    return res


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        L, X = map(int, input().split())
        C = input()

        if L == 1 or len(set(C)) == 1:
            print(f'Case #{case}: NO')
            continue

        if multiply(C, X) != -1:
            print(f'Case #{case}: NO')
            continue

        S = C * min(X, 8)

        if check_string(S):
            print(f'Case #{case}: YES')
        else:
            print(f'Case #{case}: NO')


main()
