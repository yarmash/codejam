def main():
    T = int(input())
    for j in range(T):
        N = int(input())
        L = [int(x) for x in input().split()]

        from collections import Counter

        c1 = Counter(L[::2])
        c2 = Counter(L[1::2])

        L.sort()
        valid = 0

        for i, v in enumerate(L):
            if i % 2 == 0:
                if c1[v]:
                    valid += 1
                    c1[v] -= 1
                else:
                    break
            else:
                if c2[v]:
                    valid += 1
                    c2[v] -= 1
                else:
                    break
        if valid == N:
            valid = 'OK'
        print('Case #{}: {}'.format(j+1, valid))


main()
