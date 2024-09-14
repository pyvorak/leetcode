class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = cnt = 0

        for num in nums:
            if num == max_num:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0

        return ans
