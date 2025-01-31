class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = []
        n = len(grid)

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n
        
        def flood(i, j, cnt):
            if not valid(i,j) or grid[i][j] != 1:
                return 0
            grid[i][j] = cnt
            return 1 + flood(i+1, j, cnt) + flood(i-1, j, cnt) + flood(i, j+1, cnt) + flood(i, j-1, cnt)

        def flip(i, j):
            cnt = 1
            seen = set()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if valid(x,y):
                    cur = grid[x][y]
                    if cur != 0 and cur not in seen:
                        seen.add(cur)
                        cnt += islands[cur-2]
            return cnt
            
        ans = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = len(islands) + 2
                    islands.append(flood(i, j, cnt))
                    ans = max(ans, islands[-1])

        if islands:
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 0:
                        ans = max(ans, flip(i, j))
        else:
            ans = max(ans, 1)

        return ans
