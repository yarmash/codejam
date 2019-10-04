#!/usr/bin/env python

"""Rounding Error"""

from heapq import heappop, heappush


# TODO: use integer arithmetic instead of floating point
def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        total_people, num_languages = map(int, input().split())
        freq = map(int, input().split())

        percent_per_person = 100/total_people
        low_scores = []
        not_responded = total_people
        res = 0

        for f in freq:
            p = f*percent_per_person
            if 0 < p-int(p) < 0.5:
                heappush(low_scores, (-(p-int(p)), p))
            else:
                res += int(p+0.5)  # Python3's round() won't work here!
            not_responded -= f

        while not_responded:
            try:
                _, p = heappop(low_scores)
            except IndexError:
                p = 0

            p += percent_per_person

            if 0 < p-int(p) < 0.5:
                heappush(low_scores, (-(p-int(p)), p))
            else:
                res += int(p+0.5)
            not_responded -= 1

        res += sum(int(x[1]+0.5) for x in low_scores)

        print('Case #{}: {}'.format(case, res))


main()
