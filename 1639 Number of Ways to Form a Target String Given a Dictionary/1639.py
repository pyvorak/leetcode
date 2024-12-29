class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        n = len(words[0])
        m = len(target)
        freq = [Counter() for _ in range(n)]

        for word in words:
            for i, c in enumerate(word):
                freq[i][c] += 1

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                dp[i][j] = (dp[i][j] + freq[i-1][target[j-1]] * dp[i-1][j-1]) % MOD
        
        return dp[n][m]
