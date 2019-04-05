#!/usr/bin/env python

"""Go, Gopher!"""


def free_cells(M, i, j):
    return sum(1 for c in (M[i][j], M[i-1][j-1], M[i-1][j], M[i-1][j+1], M[i][j+1],
                           M[i+1][j+1], M[i+1][j], M[i+1][j-1], M[i][j-1]) if not c)


def main():
    T = int(input())
    for i in range(T):
        A = int(input())  # minimum area
        M = [[0]*1000 for _ in range(1000)]

        candidates = [(x, y) for x in range(500+1, 500+4-1) for y in range(500+1, 500+A//4-1)]

        I = J = None

        while not (I == J == 0):
            c = max(candidates, key=lambda c: free_cells(M, c[0], c[1]))
            print(c[0], c[1], flush=True)
            I, J = map(int, input().split())
            if I == J == -1:
                return

            M[I][J] = 1


main()
