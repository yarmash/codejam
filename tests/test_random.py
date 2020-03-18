"""Tests for the functions in the codejam.random module."""

import pytest

from codejam.random import select_random_item


class TestSelectRandomItem:
    """Tests for the select_random_item() function"""

    @pytest.mark.parametrize('iterable', [
        123,
        {1, 2, 3},
        {1: 1, 2: 2, 3: 3},
        frozenset('abc'),
    ])
    def test_invalid_types(self, iterable):
        with pytest.raises(TypeError):
            select_random_item(iterable)

    @pytest.mark.parametrize('args,item', [
        # sequences
        [[''], None],
        [['', 'foo'], 'foo'],
        [['a'], 'a'],
        [['abc'], 'b'],
        # iterators
        [[iter(())], None],
        [[iter(()), 'foo'], 'foo'],
        [[iter('a')], 'a'],
        [[iter('abc')], 'c'],
    ])
    def test_select_random_item(self, args, item, random_seed):
        assert select_random_item(*args) == item

    def test_iterator_exhausted(self, random_seed):
        iterator = iter('abc')
        assert select_random_item(iterator) == 'c'
        assert next(iterator, None) is None
