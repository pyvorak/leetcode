class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        return sum(1 for i in range(len(s1)) if s1[i] != s2[i]) == 2
