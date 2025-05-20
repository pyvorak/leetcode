class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        a = [0]*(n+1)

        for l, r in queries:
            a[l] += 1
            a[r+1] -= 1

        cnt = 0

        for i, x in enumerate(nums):
            cnt += a[i]
            if x > cnt:
                return False

        return True
