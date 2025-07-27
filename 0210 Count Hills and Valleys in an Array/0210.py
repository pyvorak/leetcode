class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        prev = nums[0]

        for i in range(1, n-1):
            cur = nums[i]
            nxt = nums[i+1]

            if cur != nxt:
                if (cur > prev and cur > nxt) or (cur < prev and cur < nxt):
                    ans += 1
                prev = cur
        
        return ans
