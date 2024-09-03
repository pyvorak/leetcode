class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        
        for c in s:
            num = ord(c) - ord('a') + 1
            if num >= 10: num = num // 10 + num % 10
            ans += num
        
        while k > 1:
            cur = ans
            ans = 0
            while cur > 0:
                ans += cur % 10
                cur //= 10
            k -= 1

        return ans
