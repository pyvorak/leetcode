class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]

        self.ans = 0

        def valid_row(r):
            return r >= 0 and r < m

        def valid_move(r, c, next_r, next_c, next_cnt):
            return valid_row(next_r) and grid[r][c] < grid[next_r][next_c] and next_cnt > dp[next_r][next_c]

        def find(r, c):
            if c < n - 1:
                next_cnt = dp[r][c] + 1
                next_c = c + 1
                for next_r in range(r-1, r+2):
                    if valid_move(r, c, next_r, next_c, next_cnt):
                        self.ans = max(self.ans, next_cnt)
                        dp[next_r][next_c] = next_cnt
                        find(next_r, next_c)

        for r in range(m):
            find(r, 0)

        return self.ans
