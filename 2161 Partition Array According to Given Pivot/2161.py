class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        equal = []
        big = []

        for num in nums:
            if num < pivot:
                small.append(num)
            elif num > pivot:
                big.append(num)
            else:
                equal.append(num)
        
        return small + equal + big
