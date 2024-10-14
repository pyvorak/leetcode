class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        
        for num in nums:
            heappush(pq, -num)

        ans = 0

        for _ in range(k):
            cur = -heappop(pq)
            ans += cur
            heappush(pq, -ceil(cur/3))

        return ans
                
