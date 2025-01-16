class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1, x2 = 0, 0
        m, n = len(nums1), len(nums2)

        if n % 2 == 1:
            for num in nums1:
                x1 ^= num
        
        if m % 2 == 1:
            for num in nums2:
                x2 ^= num

        return x1 ^ x2
