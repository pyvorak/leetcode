class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        a = []
        prev = -float("inf")
        for x, i in sorted([(x, i) for i, x in enumerate(nums)]):
            if x - prev <= limit:
                a[-1][0].append(i)
                a[-1][1].append(x)
            else:
                a.append([[i],[x]])
            prev = x

        for idx, val in a:
            for i, x in zip(sorted(idx), sorted(val)):
                nums[i] = x
        
        return nums 
        
