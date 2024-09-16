class Solution:
    def findMinDifference(self, times: List[str]) -> int:
        def mins(time):
            h, m = [int(x) for x in time.split(':')]
            return h * 60 + m
            
        times.sort()
        ans = 24 * 60 - mins(times[-1]) + mins(times[0])
        for i in range(1, len(times)):
            ans = min(ans, mins(times[i]) - mins(times[i-1]))
        return ans
