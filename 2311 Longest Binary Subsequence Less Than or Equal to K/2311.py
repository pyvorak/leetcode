class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = z = s.count('0')
        x = 1
        cur = 0

        for i, c in enumerate(s[::-1]):
            if c == '0':
                z -= 1
            else:
                cur += x
                cnt = i + 1 + z
                if cur > k or cnt <= ans:
                    break
                else:
                    ans = cnt
            x *= 2
        
        return ans

        
