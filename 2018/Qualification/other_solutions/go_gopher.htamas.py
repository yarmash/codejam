import sys

T = int(input())
for t in range(1, T+1):
    A = int(input())
    h, w, a = (2, 3, 6) if A == 20 else (12, 13, 156)
    O, N = set(), [0 for _ in range(a)]
    while True:
        c = min(range(a), key=N.__getitem__)
        print(c//w+2, c%w+2)
        sys.stdout.flush()
        p, q = map(int, input().split())
        if (p, q) == (0, 0): break
        if (p, q) == (-1, -1): exit()
        if (p, q) not in O:
            O.add((p, q))
            for i in range(p-3, p):
                for j in range(q-3, q):
                    if 0<=i<h and 0<=j<w:
                        N[i*w+j] += 1
