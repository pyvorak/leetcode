class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        seen = [False] * 100001
        ans = -1

        for num in nums:
            seen[num] = True
        
        for num in nums:
            cnt = 1
            next_num = num * num

            while next_num <= nums[-1] and seen[next_num]:
                cnt += 1
                next_num *= next_num
            
            if cnt >= 2:
                ans = max(ans, cnt)    

        return ans
