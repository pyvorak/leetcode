class Solution:
    def minimumLength(self, s: str) -> int:
        return len(s) - sum(x - 2 if x % 2 == 0 else x - 1 for x in Counter(s).values())
