class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x = 2**maximumBit - 1
        return [x := x ^ num for num in nums][::-1]
