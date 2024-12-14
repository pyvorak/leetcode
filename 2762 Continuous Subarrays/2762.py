class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        l = 0
        ans = 0

        for r in range(n):
            freq[nums[r]] += 1

            while max(freq) - min(freq) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            ans += r - l + 1

        return ans
