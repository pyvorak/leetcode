class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p
        
        if target == 0:
            return 0

        ans = n
        d = {0: -1}
        cur = 0

        for i in range(n):
            cur = (cur + nums[i]) % p
            
            prev = (cur - target + p) % p
            if prev in d:
                ans = min(ans, i - d[prev])

            d[cur] = i

        return -1 if ans == n else ans
