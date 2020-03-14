#!/usr/bin/env python

"""Fair Fight"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, K = map(int, input().split())

        C = dict(enumerate(map(int, input().split()), 1))  # Charles' skill levels for each type of sword
        D = dict(enumerate(map(int, input().split()), 1))  # Delila's skill levels for each type of sword

        cnt = 0

        for L in range(1, N+1):
            for R in range(L, N+1):
                c = max(map(C.get, range(L, R+1)))
                d = max(map(D.get, range(L, R+1)))

                if abs(c-d) <= K:
                    cnt += 1

        print('Case #{}: {}'.format(case, cnt))


main()
