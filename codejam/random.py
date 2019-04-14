import random


def select_random(iterable, default=None, random=random):
    """
    Select a random element from an iterable.
    Return default if iterable is empty.

    If iterable is a sequence then `random.choice()` is used for efficiency.
    If iterable is an iterator, reservoir sampling is used (exhausts the iterator).
    """
    try:
        return random.choice(iterable)  # O(1) time and space
    except IndexError:  # empty sequence
        return default
    except TypeError:  # not a sequence
        return select_random_it(iter(iterable), default, random.randrange)


def select_random_it(iterator, default=None, randrange=random.randrange):
    """
    Return a random element from iterator (exhausting the iterator).
    Return default if iterator is empty.
    O(n) time, O(1) space algorithm.
    """
    # from https://stackoverflow.com/a/1456750/4279
    # select 1st item with probability 100% (if input is one item, return it)
    # select 2nd item with probability 50% (or 50% the selection stays the 1st)
    # select 3rd item with probability 33.(3)%
    # select nth item with probability 1/n
    selection = default
    for i, item in enumerate(iterator, start=1):
        if randrange(i) == 0:  # random in range [0..i)
            selection = item
    return selection
