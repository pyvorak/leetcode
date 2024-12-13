class Solution:
    def findScore(self, nums: List[int]) -> int:
        seen = set()
        ans = 0

        for x, i in sorted([(x, i) for i, x in enumerate(nums)]):
            if i not in seen:
                ans += nums[i]
                seen.update([i-1, i, i+1])

        return ans
