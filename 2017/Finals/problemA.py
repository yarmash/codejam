#!/usr/bin/env python

from collections import defaultdict
from itertools import groupby


def straights(chunk, idx):
    """Generate straights for a chunk starting at index idx"""

    if idx == len(chunk) - 1:
        yield idx + 1
        return

    for x in chunk[idx]:
        new_chunk = chunk.copy()

        for i in range(idx+1, len(chunk)):
            new_chunk[i] = new_chunk[i].copy()
            new_chunk[i].discard(x)

            if not new_chunk[i]:
                yield idx + 1
                break
        else:
            yield from straights(new_chunk, idx+1)


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
        integers = defaultdict(set)

        for j in range(ndice):
            for integer in map(int, input().split()):
                integers[integer].add(j)

        #print(integers)
        chunks = []

        # find runs of consecutive numbers
        for k, g in groupby(enumerate(sorted(integers)), lambda x: x[0]-x[1]):
            g = list(g)
            if len(g) > 1:
                chunks.append(list(map(lambda x: integers[x[1]], g)))

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


                for straight in straights(subchunk, 0):
                    #print(straight)
                    if straight > max_straight:
                        #print("--> NEW MAX STRAIGHT: ", straight)
                        max_straight = straight
                        if straight == len(subchunk):
                            break

        print("Case #{}: {}".format(i+1, max_straight))

main()
