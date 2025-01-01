class Solution:
    def maxScore(self, s: str) -> int:
        zero = s[0].count('0')
        one = s[1:].count('1')
        ans = zero + one

        for i in range(1, len(s)-1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            ans = max(ans, zero + one)
            
        return ans
