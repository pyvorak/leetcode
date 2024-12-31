class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [float('inf')] * (last_day+1)
        dp[0] = 0

        i = 0
        for day in range(1, last_day + 1):
            if day < days[i]:
                dp[day] = dp[day-1]
            else:
                for d, cost in zip([1,7,30], costs):
                    prev_day = max(0, day - d)
                    dp[day] = min(dp[day], dp[prev_day] + cost)
                i += 1

        return dp[last_day]
