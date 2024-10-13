class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = -float("inf")
        
        for i in range(len(nums)):
            val = nums[i][0]
            heappush(min_heap, (val, i, 0))
            max_val = max(max_val, val)

        ans = [-10**5, 10**5]        

        while min_heap:
            val, i, j = heappop(min_heap)

            if max_val - val < ans[1] - ans[0]:
                ans = [val, max_val]

            if j + 1 < len(nums[i]):
                next_val = nums[i][j + 1]
                heappush(min_heap, (next_val, i, j + 1))
                max_val = max(max_val, next_val)
            else:
                break

        return ans
