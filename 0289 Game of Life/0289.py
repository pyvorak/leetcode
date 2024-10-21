class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def next_state(x, y):
            live = 0
            
            for i in range(max(x-1, 0), min(x+1, m-1) + 1):
                for j in range(max(y-1, 0), min(y+1, n-1) + 1):
                    if not (x == i and y == j) and (board[i][j] == 1 or board[i][j] == 3):
                        live += 1

            if board[x][y] == 1 and not (live == 2 or live == 3):
                board[x][y] = 3
            elif board[x][y] == 0 and live == 3:
                board[x][y] = 2

        for i in range(m):
            for j in range(n):
                next_state(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
