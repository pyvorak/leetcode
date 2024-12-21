class TrieNode:
    def __init__(self):
        self.count = 0
        self.next = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.ans = 0

    def add(self, word):
        cur = self.head
        for key in zip(word, reversed(word)):
            cur = cur.next[key]
            self.ans += cur.count
        cur.count += 1

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.add(word)
        return t.ans
