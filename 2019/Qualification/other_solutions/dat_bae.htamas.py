#!/usr/bin/env python3

Q = ['00000000000000001111111111111111' * 32, '0000000011111111' * 64,
     '00001111' * 128, '0011' * 256, '01' * 512]

T = int(input())
for t in range(1, T+1):
    N, B, F = map(int, input().split()) 
    # we assume N <= 1024, B <= 15 and F == 5
    R = []
    for q in Q:
        print(q[:N], flush=True)
        r = input()
        if r == '-1': exit()
        R.append(r)
    C = set()
    l = 0
    for i in zip(*R):
        v = l & ~31 | int(''.join(i), 2)
        if v < l: v += 32
        C.add(v)
        l = v
    E = sorted(set(range(N))-C)
    print(' '.join(map(str, E)), flush=True)
    r = input()
    if r == '-1': exit()

