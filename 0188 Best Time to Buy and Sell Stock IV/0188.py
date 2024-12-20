class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[float('inf'), 0] for _ in range(k)]

        for price in prices:    
            prev_profit = 0
            for i in range(k):
                cur_buy, cur_profit = dp[i]

                cur_buy = min(cur_buy, price - prev_profit)
                cur_profit = max(cur_profit, price - cur_buy)
                
                dp[i] = [cur_buy, cur_profit]
                prev_profit = cur_profit

        return dp[-1][1]
