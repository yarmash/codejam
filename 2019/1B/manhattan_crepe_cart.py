#!/usr/bin/env python

"""Manhattan Crepe Cart"""

from itertools import repeat


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        P, Q = map(int, input().split())  # the number of people, and the maximum value of an x or y coordinate

        axis_x = [0]*(Q+1)
        axis_y = [0]*(Q+1)

        for _ in repeat(None, P):
            X, Y, D = input().split()  # D is one of N, S, E, W

            if D == 'N':
                for i in range(int(Y)+1, Q+1):
                    axis_y[i] += 1
                for i in range(Q+1):
                    axis_x[i] += 1
            elif D == 'S':
                for i in range(int(Y)):
                    axis_y[i] += 1
                for i in range(Q+1):
                    axis_x[i] += 1
            elif D == 'E':
                for i in range(int(X)+1, Q+1):
                    axis_x[i] += 1
                for i in range(Q+1):
                    axis_y[i] += 1
            else:  # 'W'
                for i in range(int(X)):
                    axis_x[i] += 1
                for i in range(Q+1):
                    axis_y[i] += 1

        print('Case #{}: {} {}'.format(case, axis_x.index(max(axis_x)), axis_y.index(max(axis_y))))


main()
