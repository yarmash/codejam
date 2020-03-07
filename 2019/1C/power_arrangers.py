#!/usr/bin/env python

"""Power Arrangers"""

from itertools import permutations


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)


def eliminate_candidate(candidates, letters):
    l = len(letters)
    t = tuple(letters)
    matches = [c for c in candidates if c[:l] == t]
    if len(matches) == 1:
        candidates.remove(matches[0])
        return True
    return False


def main():
    T, F = map(int, input().split())  # the number of test cases and the number of figures allowed to inspect
    arrangers = {'A', 'B', 'C', 'D', 'E'}
    perms = list(permutations(arrangers))

    for _ in range(T):
        candidates = perms[:]

        for chunk in grouper(range(1, 596), 5):
            letters = []
            for figure in chunk:
                print(figure, flush=True)
                letter = input()
                if letter == 'N':
                    return
                letters.append(letter)
                if eliminate_candidate(candidates, letters):
                    break

        print(''.join(candidates[0]), flush=True)
        result = input()
        if result == 'N':
            return


main()
