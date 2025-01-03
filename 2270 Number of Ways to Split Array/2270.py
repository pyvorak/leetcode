class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        ans = 0

        for num in nums[:-1]:
            l += num
            r -= num
            if l >= r:
                ans += 1
            
        return ans
