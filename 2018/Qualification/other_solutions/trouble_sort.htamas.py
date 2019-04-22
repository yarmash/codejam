T = int(input())
for t in range(1, T+1):
    N = int(input())
    V = [int(i) for i in input().split()]
    S = [sorted(V[::2]), sorted(V[1::2])]
    m = next((i for i in range(N-1) if S[i%2][i//2] > S[(i+1)%2][(i+1)//2]), 'OK')
    print('Case #{}: {}'.format(t, m))
