class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        a = sum(grid[0])
        b = 0
        ans = float("inf")

        for i in range(len(grid[0])):
            a -= grid[0][i]
            ans = min(ans, max(a,b))
            b += grid[1][i]
        
        return ans
