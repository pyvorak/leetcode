class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {c:0 for c in "abc"}
        ans = l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while all(d.values()):
                d[s[l]] -= 1
                l += 1
            ans += l
        return ans
        
