def calc_damage(s):
    damage = 0
    strength = 1

    for x in s:
        if x == 'S':
            damage += strength
        else:
            strength *= 2

    return damage


def swap_one(L):
    for i in range(len(L)-1):
        if L[i] == 'C' and L[i+1] == 'S':
            L[i], L[i+1] = L[i+1], L[i]
            return True
    return False


def calc_hacks(D, P):
    d = calc_damage(P)
    h = 0

    if d > D:
        if 'C' not in P:
            h = 'IMPOSSIBLE'
        else:
            L = list(P)
            while swap_one(L):
                h += 1
                d = calc_damage(L)
                if d <= D:
                    break

        if d > D:
            h = 'IMPOSSIBLE'

    return h


def main():
    T = int(input())

    for i in range(T):
        D, P = input().split()
        D = int(D)
        h = calc_hacks(D, P)
        print('Case #{}: {}'.format(i+1, h))


main()
