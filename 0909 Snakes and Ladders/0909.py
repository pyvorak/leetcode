class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_next_square(position):
            q, r = divmod(position-1, n)
            row = n - 1 - q
            col = n - 1 - r if q % 2 != 0 else r
            return position if board[row][col] == -1 else board[row][col] 

        pq = [(0, 1)]
        seen = [False]*(n*n+1)

        while pq:
            moves, position = heappop(pq)
            
            if position == n*n:
                return moves

            for next_position in range(position+1, min(position+6, n*n) + 1):
                next_square = get_next_square(next_position)
                
                if not seen[next_square]:
                    seen[next_square] = True
                    heappush(pq, (moves+1, next_square))

        return -1 
