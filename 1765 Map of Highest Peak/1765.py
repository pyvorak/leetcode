class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = -1

        while q:
            i, j = q.popleft()
            for x, y in ((0,1), (0,-1), (1, 0), (-1,0)):
                a = i + x
                b = j + y
                if 0 <= a < m and 0 <= b < n and isWater[a][b] == -1:
                    isWater[a][b] = isWater[i][j] + 1
                    q.append((a, b))

        return isWater
