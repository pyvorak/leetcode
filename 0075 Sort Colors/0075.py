class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = -1
        b = len(nums)
        i = 0

        while i < b:
            x = nums[i]
            if x == 0:
                r += 1 
                nums[i], nums[r] = nums[r], nums[i]
                i += 1
            elif x == 2:
                b -= 1
                nums[i], nums[b] = nums[b], nums[i]
            else:
                i += 1 
        
