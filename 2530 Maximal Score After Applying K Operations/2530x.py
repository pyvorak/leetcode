class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums := [-num for num in nums])
        for _ in range(k): ans += heappushpop(nums, floor(nums[0]/3))
        return -ans
                
