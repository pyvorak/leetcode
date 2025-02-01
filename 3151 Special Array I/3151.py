class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0] & 1

        for num in nums[1:]:
            cur = num & 1
            if cur == prev:
                return False
            prev ^= 1

        return True
