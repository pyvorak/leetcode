class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(s1.split() + s2.split())
        return [x for x in c if c[x] == 1]
