class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""

        for c in s:
            if not (len(ans) >= 2 and c == ans[-1] and c == ans[-2]):
                ans += c

        return ans
