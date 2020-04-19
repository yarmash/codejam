#!/usr/bin/env python3

"""Expogo"""

from collections import deque


def search(X, Y):
    if (X + Y) % 2 == 0:
        return 'IMPOSSIBLE'

    d = deque((
        ((0, 1), 0, 'N'),
        ((1, 0), 0, 'E'),
        ((-1, 0), 0, 'W'),
        ((0, -1), 0, 'S')
    ))

    while d:
        (x, y), i, path = d.popleft()

        if x == X and y == Y:
            return path

        d.append(((x, y+2**(i+1)), i+1, path+'N'))
        d.append(((x+2**(i+1), y), i+1, path+'E'))
        d.append(((x, y-2**(i+1)), i+1, path+'S'))
        d.append(((x-2**(i+1), y), i+1, path+'W'))


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        X, Y = map(int, input().split())  # the coordinates of the goal point

        res = search(X, Y)
        print('Case #{}: {}'.format(case, res))


main()
