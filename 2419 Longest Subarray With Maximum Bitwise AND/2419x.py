class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        return max(len(list(a)) for x, a in groupby(nums) if x == max_num)
