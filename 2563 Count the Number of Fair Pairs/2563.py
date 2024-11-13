class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in range(n):
            low = bisect_left(nums, lower - nums[i], i + 1, n)
            high = bisect_right(nums, upper - nums[i], i + 1, n)
            ans += high - low
        
        return ans
