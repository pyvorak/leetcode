class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        f = False
        flip = [f] * n
        
        ans = 0
        
        for i, b in enumerate(nums):
            if flip[i]:
                f = not f

            if b == f:
                f = not f
                ans += 1
                j = i + 3 
                if j > n:
                    return -1
                elif j < n:
                    flip[j] = not flip[j]
        
        return ans
