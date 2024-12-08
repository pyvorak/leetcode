class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        seen = []
        ans, best = 0, 0

        for start, end, value in events:
            while seen and seen[0][0] < start:
                best = max(best, seen[0][1])
                heappop(seen)

            ans = max(ans, best + value)
            
            heappush(seen, [end, value])

        return ans
