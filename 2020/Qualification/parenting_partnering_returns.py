#!/usr/bin/env python3

"""Parenting Partnering Returns"""


def main():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())  # the number of activities to assign
        activities = [(i, tuple(map(int, input().split()))) for i in range(N)]

        activities.sort(key=lambda x: x[1][0])

        C = J = [0, 0]
        res = []

        for i, a in activities:
            if a[0] >= C[1]:
                res.append((i, 'C'))
                C = a
            elif a[0] >= J[1]:
                res.append((i, 'J'))
                J = a
            else:
                print('Case #{}: IMPOSSIBLE'.format(case))
                break
        else:
            res.sort(key=lambda x: x[0])

            print('Case #{}: {}'.format(case, ''.join(x[1] for x in res)))


main()
