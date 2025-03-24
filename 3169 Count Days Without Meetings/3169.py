class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        n = len(meetings)
        i = ans = prev =  0

        while i < n:
            start, end = meetings[i]
            ans += start - prev - 1

            while i+1 < n and meetings[i+1][0] <= end + 1:
                end = max(end, meetings[i+1][1])
                i += 1
            
            prev = end
            i += 1
        
        ans += days - prev
        
        return ans
