class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        a = sorted(nums.copy())

        def valid(i):
            for r, x in enumerate(a):
                if x != nums[(i+r) % n]:
                    return False
            return True

        for i in range(n):
            if valid(i):
                return True

        return False
