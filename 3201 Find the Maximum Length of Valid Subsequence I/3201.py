class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = cnt = 0
        prev = None

        for x in nums:
            x %= 2
            
            if x != prev:
                cnt += 1
                prev = x

            if x % 2 == 0:
                even += 1
            else:
                odd += 1

        return max(odd, even, cnt)
