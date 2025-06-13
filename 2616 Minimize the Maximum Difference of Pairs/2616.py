class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()
        n = len(nums)

        if p == 1:
            return min(nums[i+1] - nums[i] for i in range(n-1))

        
        def valid(x):
            i = 0
            cnt = 0
            
            while i + 1 < n:
                if nums[i+1] - nums[i] <= x:
                    i += 1
                    cnt += 1
                if cnt >= p:
                    return True
                i += 1

            return False
        
        l = 0
        ans = r = nums[-1] - nums[0]

        while l <= r:
            m = (l+r)//2

            if valid(m):
                r = m - 1                
                ans = m
            else:
                l  = m + 1
        
        return ans

