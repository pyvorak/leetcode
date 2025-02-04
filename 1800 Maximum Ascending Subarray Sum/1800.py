class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = cnt = prev = nums[0]

        for num in nums:
            cnt = cnt + num if num > prev else num
            ans = max(ans, cnt)
            prev = num

        return ans
