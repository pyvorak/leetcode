class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans, l, r = 0, 0, 0

        for num in arr:
            if num % 2 == 0:
                l += 1
            else:
                l, r = r, l
                r += 1
            ans = (ans + r) % MOD

        return ans
