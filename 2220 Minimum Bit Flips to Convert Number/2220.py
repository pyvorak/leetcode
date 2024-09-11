class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        flips = start ^ goal

        while flips:
            ans += flips & 1
            flips //= 2
        
        return ans
