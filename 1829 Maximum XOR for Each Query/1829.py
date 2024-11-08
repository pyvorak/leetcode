class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_value = 2**maximumBit - 1
        cur = 0

        for num in nums:
            cur ^= num

        ans = []
        n = len(nums)
        for num in nums[::-1]:
            k = max_value ^ cur
            ans.append(k)
            cur ^= num

        return ans
