class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0

        for y in range(k):
            dp = [0] * k
            for x in nums:
                x %= k
                dp[x] = dp[y-x] + 1
            ans = max(ans, max(dp))
        
        return ans
