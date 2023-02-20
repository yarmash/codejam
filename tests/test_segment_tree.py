"""Tests for the SegmentTree class."""

import random
from functools import reduce

import pytest
from codejam.segment_tree import SegmentTree

SEQ_LEN = 100


@pytest.fixture
def random_seq():
    return [random.randint(-1000, 1000) for _ in range(SEQ_LEN)]


@pytest.fixture(params=['max', 'min', 'sum'])
def segment_tree(random_seq, request):
    return SegmentTree(random_seq, query_type=request.param)


@pytest.mark.parametrize('left,right', [(0, 0), (0, SEQ_LEN-1), (10, SEQ_LEN-10)])
def test_query(random_seq, segment_tree, left, right):
    # Note: we can't use `segment_tree.func` directly here, because that is generally
    # a function of two arguments, while in the test we need a function that works on a range.
    assert segment_tree.query(left, right) == reduce(segment_tree.func, random_seq[left:right+1])


@pytest.mark.parametrize('pos,value', [(0, -10**5), (SEQ_LEN//2, 10**5), (SEQ_LEN-1, -10**5)])
def test_modify(random_seq, segment_tree, pos, value):
    segment_tree.modify(pos, value)
    random_seq[pos] = value
    assert segment_tree.query(0, SEQ_LEN-1) == reduce(segment_tree.func, random_seq)
