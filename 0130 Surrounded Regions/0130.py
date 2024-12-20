class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        O, X = 'O', 'X'

        def flood(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == O:
                board[i][j] = None
                for x, y in [[0,1], [0,-1], [1, 0], [-1, 0]]:
                    flood(i+x, j+y)

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == O:
                    flood(i, j)
        
        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == O:
                    flood(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != X:
                    board[i][j] = X if board[i][j] else O
