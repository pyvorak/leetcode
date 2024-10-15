class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, cur, reach = 0, 0, 0
        
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == cur:
                jumps += 1
                cur = reach
        
        return jumps
