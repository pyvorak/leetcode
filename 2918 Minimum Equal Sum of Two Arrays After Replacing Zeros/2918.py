class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.count(0)
        b = nums2.count(0)
        x = sum(nums1)
        y = sum(nums2)

        if a == 0 and b == 0:
            return x if x == y else -1
        elif a == 0:
            return x if x >= y + b else -1
        elif b == 0:
            return y if y >= x + a else -1
        else:
            return max(x + a, y + b)
