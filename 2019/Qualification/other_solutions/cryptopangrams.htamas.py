#!/usr/bin/env python3

from math import gcd

T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    S = [int(i) for i in input().split()]
    e = [None] * (L+1)
    p = next(i for i in range(L-1) if S[i] != S[i+1])
    e[p+1] = gcd(S[p], S[p+1])
    for i in range(p, -1, -1):
        e[i] = S[i]//e[i+1]
    for i in range(p+2, L+1):
        e[i] = S[i-1]//e[i-1]
    d = dict(zip(sorted(set(e)), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    r = ''.join(d[i] for i in e)
    print('Case #{}: {}'.format(t, r))
