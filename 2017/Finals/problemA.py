#!/usr/bin/env python

from collections import defaultdict
from itertools import groupby


def straights(chunk, idx, free_dice):
    """Generate straights for a chunk starting at index idx"""

    if idx == len(chunk) - 1:
        yield idx + 1
    else:
        for x in chunk[idx]:
            if x in free_dice:
                yield from straights(chunk, idx+1, free_dice.difference((x,)))
            else:
                yield idx + 1


def check_dice(chunk):
    """Check that chunk has enough unique dice to form a solution."""

    # number of unique dice should be greater than or equal to the length of the chunk
    for i in range(len(chunk), 1, -1):
        for j in range(0, len(chunk)-i+1, i):
            subchunk = chunk[j:j+i]

            if len(set().union(*subchunk)) < len(subchunk):
                return False

    return True


def get_subchunks(chunk):
    """Generate subchunks from biggest to smallest."""
    yield chunk

    for size in range(len(chunk) - 1, 1, -1):
        for i in range(len(chunk) - size + 1):
            yield chunk[i:i+size]


def main():
    T = int(input())

    for i in range(T):
        ndice = int(input())
        integers = defaultdict(list)

        for j in range(ndice):
            for integer in map(int, input().split()):
                integers[integer].append(j)

        #print(integers)
        chunks = []

        # find runs of consecutive numbers
        for k, g in groupby(enumerate(sorted(integers)), lambda x: x[0]-x[1]):
            g = list(g)
            if len(g) > 1:
                chunks.append([integers[x[1]] for x in g])

        chunks.sort(key=len, reverse=True)

        max_straight = 1

        for chunk in chunks:
            #print(f"CHUNK of length {len(chunk)}: ", chunk)

            if len(chunk) <= max_straight:
                #print("BREAK (too small chunk)")
                break

            for subchunk in get_subchunks(chunk):
                #print(f"-> SUBCHUNK of length {len(subchunk)}: ", subchunk)

                if len(subchunk) <= max_straight:
                    #print("--> BREAK (too small subchunk)")
                    break

                if not check_dice(subchunk):
                    #print("--> CONTINUE (not enough dice)", subchunk)
                    continue


                for straight in straights(subchunk, 0, set(range(ndice))):
                    #print(straight)
                    if straight > max_straight:
                        #print("--> NEW MAX STRAIGHT: ", straight)
                        max_straight = straight
                        if straight == len(subchunk):
                            break

        print("Case #{}: {}".format(i+1, max_straight))

main()
