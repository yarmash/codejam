from functools import reduce


def main():
    def gen_sums(total, freq, remaining):
        #print(total, freq, remaining)
        if not remaining:
            #print(total, freq)
            yield reduce(lambda x, y: x + (y*100+total//2)//total, freq, 0)
        else:
            seen = set()

            for i in range(len(freq)):
                if not freq[i] in seen:
                    yield from gen_sums(total, freq[:i] + [freq[i]+1] + freq[i+1:], remaining-1)
                    seen.add(freq[i])

            yield from gen_sums(total, freq+[1], remaining-1)

    T = int(input())

    for i in range(1, T+1):
        total_people, num_languages = map(int, input().split())
        languages_frequency = [int(x) for x in input().split()]

        if not 100 % total_people:
            print('Case #{}: {}'.format(i, 100))
            continue

        #assert(len(languages_frequency) == num_languages)
        not_responded = total_people - sum(languages_frequency)


        #print(total_people, num_languages, not_responded, languages_frequency)
        max_percentage = max(gen_sums(total_people, languages_frequency, not_responded))

        print('Case #{}: {}'.format(i, max_percentage))

main()
