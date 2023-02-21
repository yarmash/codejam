from collections import defaultdict


class Trie:
    def __init__(self):
        trie = lambda: defaultdict(trie)
        self.trie = trie()

    def insert(self, word: str):
        curr = self.trie
        for c in word:
            curr = curr[c]
        curr[None] = None

    def search(self, word: str, prefix: bool = False) -> bool:
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return prefix or None in curr
