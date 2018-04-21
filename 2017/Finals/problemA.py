#!/usr/bin/env python

from collections import defaultdict
from itertools import groupby


def get_straight(chunk, idx, straight) -> int:
    """Get max straight starting at index idx."""
    #print(chunk, idx, straight)

    if idx == len(chunk) - 1:
        yield straight

    for x in chunk[idx]:
        new_chunk = chunk[:]

        for i in range(idx+1, len(chunk)):
            new_chunk[i] = new_chunk[i] - {x}
            if not new_chunk[i]:
                break
        else:
            yield from get_straight(new_chunk, idx+1, straight+1)


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


                for straight in get_straight(subchunk, 0, 1):
                    if straight > max_straight:
                        #print("--> NEW STRAIGHT: ", straight)
                        max_straight = straight
                        if straight == len(subchunk):
                            break

        print("Case #{}: {}".format(i+1, max_straight))

main()
