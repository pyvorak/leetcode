class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for c in s:
            if c.isalpha():
                ans.append(c)
            else:
                ans.pop()

        return "".join(ans)
