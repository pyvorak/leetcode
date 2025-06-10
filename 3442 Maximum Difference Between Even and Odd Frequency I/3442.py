class Solution:
    def maxDifference(self, s: str) -> int:
        a1 = -float('inf')
        a2 = float('inf')
        for x in Counter(s).values():
            if x % 2 == 1:
                a1 = max(a1, x)
            else:
                a2 = min(a2, x)
        return a1 - a2
