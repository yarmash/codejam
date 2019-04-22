from math import sqrt, sin, cos, atan
eps = 1e-12

T = int(input())
for t in range(1, T+1):
    A = float(input())
    l, L, h, H = 0, 1, atan(sqrt(2)), sqrt(3)
    while h-l > eps:
        m = (h+l)/2
        M = cos(m) + sqrt(2)*sin(m)
        if A < M:
            h, H = m, M
        else:
            l, L = m, M
    u = 2*sqrt(2)
    print('Case #{}:'.format(t))
    print(cos(l)/u, sin(l)/u, 1/u)
    print(-sin(l)/2, cos(l)/2, 0)
    print(cos(l)/u, sin(l)/u, -1/u)
