class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(len(s)):
            prev, cur = s[i-1], s[i]
            if prev[-1] != cur[0]:
                return False
        return True
