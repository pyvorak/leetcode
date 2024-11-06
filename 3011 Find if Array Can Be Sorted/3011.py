class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        small = big = nums[0]
        prev = nums[0].bit_count()
        ans = []

        for num in nums[1:]:
            cur = num.bit_count()
            if cur == prev:
                small = min(small, num)
                big = max(big, num)
            else:
                ans.append([small, big])
                small = big = num
            prev = cur
        ans.append([small, big])
        
        for i in range(1, len(ans)):
            if ans[i-1][1] > ans[i][0]:
                return False

        return True


