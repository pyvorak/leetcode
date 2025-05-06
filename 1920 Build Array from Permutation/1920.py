class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        for i, x in enumerate(nums):
            ans[i] = nums[x]
        return ans
