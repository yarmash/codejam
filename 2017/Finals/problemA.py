from operator import itemgetter
from itertools import groupby


def get_straight(chunk: list, idx: int, straight: int, dice: set) -> int:
    if idx == len(chunk) - 1:
        return straight

    item = chunk[idx]

    return max((get_straight(chunk, idx+1, straight+1, dice-{x}) for x in item[1] if x in dice), default=straight)


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
            if len(chunk) <= max_straight:
                break

            for k in range(len(chunk)-1):
                if len(chunk) - k < max_straight:
                    break
                dice = set(range(ndice))
                straight = get_straight(chunk, k, 0, dice)
                if straight > max_straight:
                    max_straight = straight

        print("Case #{}: {}".format(i+1, max_straight))

main()
