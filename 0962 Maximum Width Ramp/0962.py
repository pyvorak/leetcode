class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        n = len(nums)

        for i in range(n):
            if not stk or nums[stk[-1]] > nums[i]:
                stk.append(i)

        ans = 0

        for i in range(n-1, -1, -1):
            while stk and nums[stk[-1]] <= nums[i]:
                ans = max(ans, i - stk.pop())
    
        return ans
        
