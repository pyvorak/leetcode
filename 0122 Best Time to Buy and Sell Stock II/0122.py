class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                ans += diff

        return ans
