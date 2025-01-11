class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(1 for f in Counter(s).values() if f % 2 != 0) <= k
