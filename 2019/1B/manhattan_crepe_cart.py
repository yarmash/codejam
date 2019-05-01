#!/usr/bin/env python

"""Manhattan Crepe Cart"""

from itertools import chain, repeat


def main():
    T = int(input())  # the number of test cases

    def get_pos(people):
        # the crepe cart must be either at position 0, or at a cell that is one cell to the right of some person
        candidates = dict.fromkeys(chain([0], [i + 1 for i, d in people if d in 'EN']), 0)

        for i in candidates:
            for j, d in people:
                if d in 'EN' and i > j or d in 'WS' and i < j:
                    candidates[i] += 1
        return max(candidates.items(), key=lambda item: (item[1], -item[0]))[0]

    for case in range(1, T+1):
        P, Q = map(int, input().split())  # the number of people, and the maximum value of an x or y coordinate
        x_axis = []
        y_axis = []
        for _ in repeat(None, P):
            X, Y, D = input().split()
            if D in 'EW':
                x_axis.append((int(X), D))
            else:
                y_axis.append((int(Y), D))

        print('Case #{}: {} {}'.format(case, get_pos(x_axis), get_pos(y_axis)))


main()
