class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        max_value = values[0]

        for i in range(1, n):
            ans = max(ans, values[i] + max_value - i)
            max_value = max(max_value, values[i] + i)
            
        return ans
