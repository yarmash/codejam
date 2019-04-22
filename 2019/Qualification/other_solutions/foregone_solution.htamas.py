#!/usr/bin/env python3

T = int(input())
for t in range(1, T+1):
    N = input()
    A = N.replace('4', '3')
    B = ''.join('1' if c=='4' else '0' for c in N).lstrip('0')
    print('Case #{}: {} {}'.format(t, A, B))

