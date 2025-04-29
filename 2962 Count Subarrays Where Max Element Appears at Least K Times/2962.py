class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = max(nums)
        cnt = l = ans = 0

        for num in nums:
            if num == x:
                cnt += 1
            while cnt >= k:
                if nums[l] == x:
                    cnt -= 1
                l += 1
            ans += l

        return ans 
