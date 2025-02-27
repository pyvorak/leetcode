class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        dp = {}

        for i, c in enumerate(arr):
            dp[c] = defaultdict(lambda: 2)
            for b in reversed(arr[:i]):
                a = c - b

                if a >= b:
                    break
                
                if a not in dp:
                    continue

                dp[b][c] = dp[a][b]+1
                ans = max(ans, dp[b][c])        

        return ans
