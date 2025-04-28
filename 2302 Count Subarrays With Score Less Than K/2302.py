class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = cnt = ans = 0
        for r, x in enumerate(nums):
            cnt += x
            while l <= r and cnt * (r - l + 1) >= k:
                cnt -= nums[l]
                l += 1
            ans += r - l + 1
        return ans
