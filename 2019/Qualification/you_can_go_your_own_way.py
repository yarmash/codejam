#!/usr/bin/env python3

"""You Can Go Your Own Way"""


def main():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())  # the dimensions of the maze
        P = input()
        path = ''.join(['S' if move == 'E' else 'E' for move in P])
        print(f'Case #{case}: {path}')


main()
