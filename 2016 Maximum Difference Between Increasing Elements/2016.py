class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        x = nums[0]

        for y in nums:
            if y > x:
                ans = max(ans, y - x)
            else:
                x = y

        return ans
