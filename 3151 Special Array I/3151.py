class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return (n := len(nums)) == 1 or all(nums[i] & 1 != nums[i+1] & 1 for i in range(n-1))
