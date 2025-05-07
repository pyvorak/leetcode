class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        seen = [[False] * n for _ in range(m)]
        seen[0][0] = True

        pq = [[0, 0, 0]]

        while pq:
            time, i, j = heappop(pq)
            
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not seen[x][y]:
                    seen[x][y] = True
                    next_time = max(time, moveTime[x][y]) + 1
                    if x == m - 1 and y == n - 1:
                        return next_time
                    heappush(pq, [next_time, x, y])
