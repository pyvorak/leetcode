class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def find(nums):
            v = [1] * n
            for i in range(n):
                for j in range(i):
                    if nums[i] > nums[j]:
                        v[i] = max(v[i], v[j] + 1)
            return v
        
        left = find(nums)
        right = find(nums[::-1])[::-1]

        ans = 0
        
        for i in range(1, n-1):
            if left[i] > 1 and right[i] > 1:
                ans = max(ans, left[i] + right[i] -1)

        return n - ans
