def main():
    T = int(input())

    for i in range(T):
        N, L = map(int, input().split())

        words = set()
        words_list = []

        for j in range(N):
            word = input().strip()
            words.add(word)
            words_list.append(word)

        if L == 1:
            print('Case #{}: {}'.format(i+1, '-'))
            continue

        def candidates(cand):
            l = len(cand)

            if l == L:
                yield cand
            else:
                for j in range(N):
                    yield from candidates(cand + [words_list[j][l]])

        for c in candidates([]):
            if ''.join(c) not in words:
                print('Case #{}: {}'.format(i+1, ''.join(c)))
                break
        else:
                print('Case #{}: {}'.format(i+1, '-'))

main()
