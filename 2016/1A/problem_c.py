#!/usr/bin/env python

"""BFFs"""

from collections import namedtuple


def main():
    Kid = namedtuple('Kid', ['id', 'bff_id'])

    T = int(input())  # the number of test cases

    for case in range(1, T+1):

        N = int(input())  # the total number of kids in the class
        kids = [Kid(i, int(v)) for i, v in enumerate(input().split(), 1)]

        longest_circle = 0
        stack = []

        for i, v in enumerate(kids):
            stack.append(([v], [*kids[:i], *kids[i+1:]]))

        while stack:
            circle, remaining = stack.pop()

            if len(circle) > longest_circle and all(v.bff_id == circle[i-1].id or v.bff_id == circle[(i+1) % len(circle)].id
                                                    for i, v in enumerate(circle)):

                longest_circle = len(circle)

            for i, v in enumerate(remaining):
                if (
                    # after adding this kid, the previous kid still is a friend with smb next to them
                    (len(circle) == 1 or circle[-1].bff_id == v.id or circle[-1].bff_id == circle[-2].id) and (
                        # this kid makes a pair on either side of the circle
                        (circle[-1].bff_id == v.id or circle[-1].id == v.bff_id or circle[0].bff_id == v.id or circle[0].id == v.bff_id) or
                        # this kid has a friend in remaining kids
                        any(kid.bff_id == v.id or kid.id == v.bff_id for kid in remaining))):

                    stack.append(([*circle, v], [*remaining[:i], *remaining[i+1:]]))

        print(f'Case #{case}: {longest_circle}')


main()
