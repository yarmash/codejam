#!/usr/bin/env python3

"""Number Guessing"""


def main():
    T = int(input())  # the number of test cases

    for _ in range(T):
        A, B = map(int, input().split())  # exclusive lower bound and inclusive upper bound
        N = int(input())  # the maximum number of guesses

        A += 1

        while A <= B:
            guess = (A + B) // 2
            print(guess, flush=True)
            res = input()

            if res == 'TOO_SMALL':
                A = guess + 1
            elif res == 'TOO_BIG':
                B = guess - 1
            else:
                break


main()
