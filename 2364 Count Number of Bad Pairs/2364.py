class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        d = defaultdict(int)

        for i, num in enumerate(nums):
            ans += i
            d[num-i] += 1
        
        for cnt in d.values():
            ans -= sum(i for i in range(cnt))

        return ans
