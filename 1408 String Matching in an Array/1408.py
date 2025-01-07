class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for w in words if ' '.join(words).count(w) > 1]
