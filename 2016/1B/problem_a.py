#!/usr/bin/env python

"""Getting the Digits"""

from collections import Counter


def gen_words(words):
    """Yield words in the order that they contain unique character(s)."""

    words = list(words)

    while words:
        for word in words:
            if set(word).difference(*[w for w in words if w != word]):
                yield word
                words.remove(word)
                break


def main():
    T = int(input())  # the number of test cases

    WORDS = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')
    w2d = dict(zip(WORDS, '0123456789'))
    w2c = {w: Counter(w) for w in WORDS}

    words = list(gen_words(WORDS))

    for case in range(1, T+1):
        S = input()
        c = Counter(S)
        number = []

        for w in words:
            while c & w2c[w] == w2c[w]:
                number.append(w2d[w])
                c -= w2c[w]

        number.sort()

        print(f'Case #{case}: ', *number, sep='')


main()
