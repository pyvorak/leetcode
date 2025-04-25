class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = cnt = 0
        d = Counter()
        d[0] = 1
        
        for num in nums:
            if num % modulo == k:
                cnt = (cnt + 1) % modulo
            ans += d[(cnt - k) % modulo]
            d[cnt] += 1

        return ans
