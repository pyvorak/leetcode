class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pq = []

        for start, end in sorted(intervals):
            if len(pq) == 0 or pq[0] >= start:
                heappush(pq, end)
            else:
                heappushpop(pq, end)
        
        return len(pq)
