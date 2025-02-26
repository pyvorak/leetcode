class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur = 0
        a = [cur]
        
        for num in nums:
            cur += num
            a.append(cur)

        return max(a) - min(a)
