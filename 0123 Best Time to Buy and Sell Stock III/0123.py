class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1, b2 = float('inf'), float('inf')
        s1, s2 = 0, 0

        for p in prices:
            b1 = min(b1, p)
            s1 = max(s1, p-b1)

            b2 = min(b2, p-s1)
            s2 = max(s2, p-b2)

        return s2
