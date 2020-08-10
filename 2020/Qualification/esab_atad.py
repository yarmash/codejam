#!/usr/bin/env python3

"""ESAb ATAd"""


def query(pos):
    """Query a position in the array."""
    print(pos, flush=True)
    val = input()
    assert val != 'N'
    return val


def main():
    T, B = map(int, input().split())  # the number of test cases and the number of bits in the array

    for _ in range(T):
        array = [None]*B
        same_pair_idx = different_pair_idx = None
        complement = complement_or_reverse = False
        idx = 0

        while None in array:
            queries = 0

            if same_pair_idx is not None:
                complement = query(same_pair_idx+1) != array[same_pair_idx]
                queries += 1

            if different_pair_idx is not None:
                complement_or_reverse = query(different_pair_idx+1) != array[different_pair_idx]
                queries += 1

            if queries & 1:  # make sure we have full pairs before each 'fluctuation'
                query(1)
                queries += 1

            if complement:
                array = ['1' if x == '0' else '0' if x == '1' else x for x in array]
                if not complement_or_reverse:
                    array.reverse()
            elif complement_or_reverse:
                array.reverse()

            for _ in range((10 - queries)//2):
                array[idx] = query(idx+1)
                array[B-idx-1] = query(B-idx)
                if same_pair_idx is None and array[idx] == array[B-idx-1]:
                    same_pair_idx = idx
                if different_pair_idx is None and array[idx] != array[B-idx-1]:
                    different_pair_idx = idx
                idx += 1

        print(''.join(array))

        val = input()
        assert val == 'Y'


main()
