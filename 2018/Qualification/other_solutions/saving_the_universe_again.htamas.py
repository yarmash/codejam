T = int(input())
for t in range(1, T+1):
    D, P = input().split()
    h, s, v, L, F = int(D), 0, 1, [], []
    for c in P:
        if c == 'S':
            h -= v
            F.extend(L)
        elif c == 'C':
            L.append(v)
            v *= 2
    for f in [0] + sorted(F, reverse=True):
        h += f
        if h >= 0: break
        s += 1
    else:
        s = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t, s))
