#!/usr/bin/env python3

"""Standing Ovation"""


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        smax, s = input().split()
        audience = to_add = 0

        for shyness, num_people in enumerate(map(int, s)):
            if num_people:
                if shyness <= audience:
                    audience += num_people
                else:
                    to_add += shyness - audience
                    audience += (shyness - audience) + num_people

        print(f'Case #{case}: {to_add}')


main()
