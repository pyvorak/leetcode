class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0        

        for num in nums:
            if nums[i] + 2*k < num:
                i += 1
        
        return len(nums) - i
