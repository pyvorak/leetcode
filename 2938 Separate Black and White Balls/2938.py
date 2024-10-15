class Solution:
    def minimumSteps(self, s: str) -> int:
        ans, swaps = 0, 0

        for c in s:
            if c == '1':
                swaps += 1
            else:
                ans += swaps

        return ans

