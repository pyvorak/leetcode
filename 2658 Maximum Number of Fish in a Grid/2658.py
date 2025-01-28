class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] <= 0:
                return 0
                
            cnt = grid[i][j]
            grid[i][j] = 0

            return cnt + dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
