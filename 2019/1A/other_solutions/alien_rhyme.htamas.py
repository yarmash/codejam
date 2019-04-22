#!/usr/bin/env python3
from collections import Counter

T = int(input())
for t in range(1, T+1):
    N = int(input())
    W = Counter(input().rjust(50) for i in range(N))
    c = 0
    for _ in range(50):
        for k, v in W.items():
            if v >= 2:
                W[k] = v-2
                c += 2
        W = Counter(s[1:] for s in W.elements())
    print('Case #{}: {}'.format(t, c))

