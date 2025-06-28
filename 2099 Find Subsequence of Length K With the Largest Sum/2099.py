class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        a = [(i, x) for i, x in enumerate(nums)]
        ans = sorted(a, reverse = True, key = lambda x: x[1])[:k]
        return [x for i, x in sorted(ans, key = lambda x: x[0])]
