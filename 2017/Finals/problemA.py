from operator import itemgetter
from itertools import groupby, chain


def get_straight(chunk: list, idx: int, straight: int, dice: set) -> int:
    """Get max straight starting at index idx."""
    if idx == len(chunk) - 1:
        yield straight

    for x in chunk[idx][1]:
        if x in dice:
            yield from get_straight(chunk, idx+1, straight+1, dice-{x})


def check_dice(chunk):
    """Check that chunk has enough unique dice to form a solution."""

    # number of unique dice should be greater than or equal to the length of the chunk
    for i in range(len(chunk), 1, -1):
        for j in range(0, len(chunk)-i+1, i):
            subchunk = chunk[j:j+i]

            if len(set(chain.from_iterable(map(itemgetter(1), subchunk)))) < len(subchunk):
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
        integers = []

        for j in range(ndice):
            integers.extend((int(x), j) for x in input().split())

        integers.sort(key=itemgetter(0))

        grouped = [(k, [x[1] for x in g]) for k, g in groupby(integers, itemgetter(0))]
        chunks = []

        # find runs of consecutive numbers
        for k, g in groupby(enumerate(grouped), lambda x: x[0]-x[1][0]):
            g = list(g)
            if len(g) > 1:
                chunks.append(list(map(itemgetter(1), g)))

        chunks.sort(key=len, reverse=True)

        max_straight = 1

        for chunk in chunks:
            #print("CHUNK: ", chunk)

            if len(chunk) <= max_straight:
                #print("BREAK (too small chunk)")
                break

            for subchunk in get_subchunks(chunk):
                #print("SUBCHUNK: ", subchunk)

                if len(subchunk) <= max_straight:
                    #print("BREAK (too small subchunk)")
                    break

                if not check_dice(subchunk):
                    #print("CONTINUE (not enough dice)", subchunk)
                    continue

                dice = set(range(ndice))

                for straight in get_straight(subchunk, 0, 1, dice):
                    if straight > max_straight:
                        #print("NEW STRAIGHT: ", straight)
                        max_straight = straight
                        if straight == len(subchunk):
                            break

        print("Case #{}: {}".format(i+1, max_straight))

main()
