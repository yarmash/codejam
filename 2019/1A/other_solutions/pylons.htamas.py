#!/usr/bin/env python3

def moves(R, C):
    assert R <= C
    if R == 2:
        assert C >= 5
        for i in range(1, C+1):
            yield 1, i
            yield 2, (i+2)%C + 1
    else:
        assert C >= 4
        sh = (R == C and R % 2 == 0)
        for i in range(1, C+1):
            for j in range(1, R+1):
                if sh and i == C and j == 1: continue
                yield j, (i+1)%C + 1 if j%2==0 else i
        if sh: yield 1, C

T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    if R + C <= 6:
        print('Case #{}: IMPOSSIBLE'.format(t))
        continue
    print('Case #{}: POSSIBLE'.format(t))
    if R <= C:
        for r, c in moves(R, C):
            print(r, c)
    else:
        for c, r in moves(C, R):
            print(r, c)

