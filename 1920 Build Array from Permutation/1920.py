class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] > 0:
                j = i
                first = nums[i]
                while nums[j] != i:
                    tmp = nums[j]
                    nums[j] = -nums[nums[j]]
                    j = tmp
                nums[j] = -first

        return [-x for x in nums]
