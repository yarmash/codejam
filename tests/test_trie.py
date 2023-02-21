"""Tests for the Trie class."""

from random import choices, randrange
from string import ascii_lowercase

import pytest
from codejam.trie import Trie

NUM_WORDS = 100
WORD_LEN = 20


@pytest.fixture
def words():
    """Generate a list of random words."""
    return [''.join(choices(ascii_lowercase, k=randrange(WORD_LEN))) for _ in range(NUM_WORDS)]


@pytest.fixture
def trie(words):
    """Build a trie from the generated words."""
    trie = Trie()

    for word in words:
        trie.insert(word)
    return trie


@pytest.fixture
def new_word():
    """Return a word that is not present in the trie."""
    return 'TEST'


def test_search(words, trie, new_word):
    """Test searching full words."""
    for word in words:
        assert trie.search(word)

    assert not trie.search(new_word)
    trie.insert(new_word)
    assert trie.search(new_word)
    assert not trie.search(new_word[:-1])
    assert not trie.search(new_word[::-1])


def test_search_prefix(words, trie, new_word):
    """Test searching for word prefixes."""
    for word in words:
        assert trie.search(word[:-1], prefix=True)

    assert not trie.search(new_word[:-1], prefix=True)
    trie.insert(new_word)
    assert trie.search(new_word, prefix=True)
    assert trie.search(new_word[:-1], prefix=True)
    assert not trie.search(new_word[::-1], prefix=True)
    assert not trie.search(new_word[-2::-1], prefix=True)
