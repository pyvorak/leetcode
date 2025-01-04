class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        
        for i in range(26):
            c = chr(ord('a') + i)

            l = s.find(c)
            if l == -1:
                continue
            r = s.rfind(c)
            
            seen = set()
            for j in range(l+1, r):
                seen.add(s[j])
            ans += len(seen)
        
        return ans
