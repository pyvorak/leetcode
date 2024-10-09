class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans, extra = 0, 0

        for c in s:
            if c == '(':
                extra += 1
            else:
                if extra == 0:
                    ans += 1
                else:
                    extra -= 1
        
        return ans + extra
