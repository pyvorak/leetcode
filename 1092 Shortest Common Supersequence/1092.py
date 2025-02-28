class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in  range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = dp[i+1][j] if dp[i+1][j] > dp[i][j+1] else dp[i][j+1]

        ans = ""
        i, j = 0, 0

        while i < m and j < n:
            if str1[i] == str2[j]:
                ans += str1[i]
                i += 1
                j += 1
            elif dp[i+1][j] > dp[i][j+1]:
                ans += str1[i]
                i += 1
            else:
                ans += str2[j]
                j += 1
        
        if i < m:
            ans += str1[i:]

        if j < n:
            ans += str2[j:]
        
        return ans
