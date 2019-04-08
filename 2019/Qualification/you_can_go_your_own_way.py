#!/usr/bin/env python

"""You Can Go Your Own Way"""


def main():
    T = int(input())

    for case in range(1, T+1):
        input()  # the dimensions of the maze, ignored
        P = input()
        path = ''.join('S' if move == 'E' else 'E' for move in P)
        print('Case #{}: {}'.format(case, path))


main()
