class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = defaultdict(list)
        for i, j in queries:
            q[i].append(j)

        d = [0] * (len(nums)+1)
        pq = []
        cur = 0

        for i, x in enumerate(nums):
            cur += d[i]

            for j in q[i]:
                heappush(pq, -j)
        
            while x > cur:
                if pq and -pq[0] >= i:
                    cur += 1
                    d[1-heappop(pq)] -= 1
                else:
                    return -1

        return len(pq)
