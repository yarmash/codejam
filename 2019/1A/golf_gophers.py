#!/usr/bin/env python

"""Golf Gophers"""

from itertools import repeat


# TODO: reduce the time complexity of the algorithm
def main():
    T, N, M = map(int, input().split())

    numbers = (7, 11, 13, 15, 16, 17)  # pairwise coprime

    for _ in repeat(None, T):
        remainders = []
        for n in numbers:
            print(*[n]*18, flush=True)

            resp = input()
            if resp == '-1':
                return

            r = sum(map(int, resp.split())) % n
            remainders.append(r)

        for m in range(1, M+1):
            for i, n in enumerate(numbers):
                if m % n != remainders[i]:
                    break
            else:
                break
        print(m)

        resp = input()
        if resp != '1':
            return


main()
