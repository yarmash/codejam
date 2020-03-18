import random
from collections.abc import Iterator, Sequence


def select_random_item(iterable, default=None):
    """
    Select a random item from a sequence or an iterator.
    Return `default` if the iterable is empty.

    If the iterable is a sequence, then `random.choice()` is used for efficiency.
    This runs in constant time and space.
    If the iterable is an iterator, reservoir sampling is used (exhausts the iterator).
    This runs in O(n) time, O(1) space.
    """
    if isinstance(iterable, Sequence):
        if iterable:  # non-empty sequence
            return random.choice(iterable)
        return default

    if isinstance(iterable, Iterator):
        selection = default
        for i, item in enumerate(iterable, start=1):
            if random.randrange(i) == 0:  # random item in range [0..i)
                selection = item
        return selection

    raise TypeError('Iterable is not of type Sequence or Iterator')
