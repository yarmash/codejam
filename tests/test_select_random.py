"""Tests for the functions in the codejam.select_random module."""

import pytest

from codejam.select_random import select_random_item


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
    @pytest.mark.usefixtures('random_seed')
    def test_select_random_item(self, args, item):
        assert select_random_item(*args) == item

    @pytest.mark.usefixtures('random_seed')
    def test_iterator_exhausted(self):
        iterator = iter('abc')
        assert select_random_item(iterator) == 'c'
        assert next(iterator, None) is None
