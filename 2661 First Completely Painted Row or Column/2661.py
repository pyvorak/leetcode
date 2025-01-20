class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n
        d = [None]*(m*n)

        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                d[val-1] = [i,j]

        ans = 0
        
        for val in arr:
            i, j = d[val-1]
            rows[i] += 1
            cols[j] += 1

            if rows[i] == n or cols[j] == m:
                return ans    
                
            ans += 1
            
        return ans
