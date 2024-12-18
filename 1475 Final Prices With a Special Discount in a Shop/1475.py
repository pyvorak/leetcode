class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        for i, p in enumerate(prices):
            while stk and prices[stk[-1]] >= prices[i]:
                prices[stk.pop()] -= prices[i]
            stk.append(i)
        return prices
