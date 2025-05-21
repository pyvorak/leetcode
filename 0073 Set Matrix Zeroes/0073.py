class Solution:
    def setd(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        d = set() 
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    d.add((i, j))

        for i, j in d:
            matrix[i] = [0] * n
            for row in matrix:
                row[j] = 0
                  
