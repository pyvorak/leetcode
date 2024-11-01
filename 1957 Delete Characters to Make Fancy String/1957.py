class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        else:
            ans = s[:2]

            for c in s[2:]:
                if c == ans[-1] and c == ans[-2]:
                    continue
                else:
                    tans += c

            return ans
