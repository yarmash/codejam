#!/usr/bin/env python

"""Power Arrangers"""

from collections import Counter


def main():
    T, F = map(int, input().split())  # the number of test cases and the number of figures allowed to inspect

    for _ in range(T):
        figures = {1: {}, 2: {}, 3: {}, 4: {}}
        missing = []

        # find out the 1st letter
        for i in range(1, 596, 5):
            print(i, flush=True)
            letter = input()
            if letter == 'N':
                return
            figures[1][i] = letter

        c = Counter(figures[1].values())

        for k, v in c.items():
            if v == 23:
                missing.append(k)
                break

        # find out the 2nd letter
        for k, v in figures[1].items():
            if v == missing[-1]:
                print(k+1, flush=True)
                letter = input()
                if letter == 'N':
                    return
                figures[2][k+1] = letter

        c = Counter(figures[2].values())

        for k, v in c.items():
            if v == 5:
                missing.append(k)
                break

        # find out the 3rd letter
        for k, v in figures[2].items():
            if v == missing[-1]:
                print(k+1, flush=True)
                letter = input()
                if letter == 'N':
                    return
                figures[3][k+1] = letter

        c = Counter(figures[3].values())

        for k, v in c.items():
            if v == 1:
                missing.append(k)
                break

        # find out the 4th letter
        for k, v in figures[3].items():
            if v == missing[-1]:
                print(k+1, flush=True)
                letter = input()
                if letter == 'N':
                    return
                figures[4][k+1] = letter

        missing.extend(set('ABCDE') - set(missing) - set(figures[4].values()))

        # find out the 5th letter
        missing.extend(set('ABCDE') - set(missing))

        print(''.join(missing))
        result = input()
        if result != 'Y':
            return


main()
