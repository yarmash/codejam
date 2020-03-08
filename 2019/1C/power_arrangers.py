#!/usr/bin/env python

"""Power Arrangers"""

from collections import defaultdict


def main():
    T, F = map(int, input().split())  # the number of test cases and the number of figures allowed to inspect

    for _ in range(T):
        sets = [i*5 for i in range(119)]  # starting position of each set
        missing = []
        for ordinal in (1, 2, 3, 5):  # number of a figure in a set
            letters = defaultdict(list)
            for s in sets:
                print(s+ordinal, flush=True)
                result = input()
                if result == 'N':
                    return
                letters[result].append(s)

            letter, sets = min(letters.items(), key=lambda item: len(item[1]))
            missing.append(letter)

        missing += set('ABCDE') - set(missing)

        print(''.join(missing))
        result = input()
        if result != 'Y':
            return


main()
