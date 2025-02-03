class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        inc, dec = 0, 0    

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]: 
                inc = i
            if nums[i-1] <= nums[i]: 
                dec = i
            ans = max(ans, i - inc + 1, i - dec + 1)
            
        return ans
