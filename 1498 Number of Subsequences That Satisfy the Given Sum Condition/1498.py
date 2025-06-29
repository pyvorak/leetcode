class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0 
        r = n - 1
        ans = 0
        MOD = 10 ** 9 + 7

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += power[r - l] % MOD
                ans %= MOD
                l += 1
                
        return ans
