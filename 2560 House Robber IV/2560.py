class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def valid(m):
            cnt = 0
            i = 0

            while i < len(nums):
                if nums[i] <= m:
                    cnt += 1
                    i += 1
                i += 1
            
            return cnt >= k

        a = sorted(set(nums))
        l = a[0]
        ans = r = a[-1]

        while l <= r:
            m = (l + r) // 2
            if valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans 

