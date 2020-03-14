#!/usr/bin/env python

"""Fair Fight"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, K = map(int, input().split())

        C = list(map(int, input().split()))  # Charles' skill levels for each type of sword
        D = list(map(int, input().split()))  # Delila's skill levels for each type of sword

        pairs = 0

        for L in range(N):
            for R in range(L, N):
                if abs(max(C[L:R+1]) - max(D[L:R+1])) <= K:
                    pairs += 1

        print('Case #{}: {}'.format(case, pairs))


main()
