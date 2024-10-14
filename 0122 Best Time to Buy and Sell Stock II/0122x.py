class Solution:
    def maxProfit(self, a: List[int]) -> int:
        return sum([a[i] - a[i-1] for i in range(1, len(a)) if a[i] > a[i-1]])
