#!/usr/bin/env python

"""Ant Stack"""


def max_stack(weights):
    capacities = [float('inf')]  # max sums of the ants' weight

    for weight in weights:
        for idx in range(len(capacities)-1, -1, -1):
            new_capacity = min(weight * 6, capacities[idx] - weight)

            if new_capacity >= 0:
                if idx + 1 >= len(capacities):
                    capacities.append(new_capacity)
                elif new_capacity > capacities[idx + 1]:
                    capacities[idx + 1] = new_capacity
    return len(capacities) - 1


def main():

    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())  # number of ants
        W = [int(x) for x in input().split()]  # weights of the ants, in increasing order of length
        W.reverse()

        ans = max_stack(W)
        print('Case #{}: {}'.format(case, ans))


main()
