class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(ord(c) - ord('0') for c in str(num))
        
        d = defaultdict(list)

        for num in nums:
            d[digit_sum(num)].append(num)

        ans = -1

        for a in d.values():
            if len(a) >= 2:
                a.sort()
                ans = max(ans, a[-1] + a[-2])
        
        return ans
