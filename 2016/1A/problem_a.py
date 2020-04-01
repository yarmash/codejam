#!/usr/bin/env python3

"""The Last Word"""

from collections import deque


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        S = input()
        word = deque(S[0])

        for i in range(1, len(S)):
            if S[i] >= word[0]:
                word.appendleft(S[i])
            else:
                word.append(S[i])

        print(f'Case #{case}: {"".join(word)}')


main()
