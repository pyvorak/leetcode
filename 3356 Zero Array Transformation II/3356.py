class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        d = [0] * (len(nums) + 1)
        cur = k = 0

        for i, num in enumerate(nums):
            while cur + d[i] < num and k < len(queries):
                l, r, val = queries[k]
                k += 1
                if r >= i:
                    d[max(l, i)] += val
                    d[r + 1] -= val

            cur += d[i]
            
            if cur < num:
                return - 1

        return k

