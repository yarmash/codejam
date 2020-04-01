#!/usr/bin/env python3

# these numbers come from the chinese remainder theorem
magic = [(17, 960960), (16, 1786785), (15, 3539536),
         (13, 2199120), (11, 2598960), (7, 1166880)]
product = 4084080

T, N, M = map(int, input().split())
for t in range(1, T+1):
    r = 0
    for i, j in magic:
        print(' '.join([str(i)] * 18), flush=True)
        a = sum(map(int, input().split()))
        r += a * j
    r %= product
    print(r)
    if input() != '1':
        exit()
