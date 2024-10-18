class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        self.ans = 0

        def find(i, val):
            if i == len(nums):
                if val == max_or:
                    self.ans += 1
            else:
                find(i + 1, val)
                find(i + 1, val | nums[i])

        find(0, 0)

        return self.ans
