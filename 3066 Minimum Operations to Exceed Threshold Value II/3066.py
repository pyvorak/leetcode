class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums)

        while len(nums) and nums[0] < k:
            ans += 1
            x = heappop(nums)
            y = heappop(nums) 
            heappush(nums, min(x, y) * 2 + max(x, y))

        return ans
