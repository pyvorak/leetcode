class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board) 

        b = [-1]
        flip = False

        for row in board[::-1]:
            if flip:
                row = row[::-1]
            b.extend(row)
            flip = not flip
        
        b = [x if x != -1 else i for i, x in enumerate(b)]

        pq = [(0, -1)]
        ans = n*n
        seen = [False] * (ans+1)
    
        while pq:
            cnt, x = heappop(pq)
            x = -x

            if x == ans:
                return cnt

            for move in range(x+1, min(x+6, ans)+1):
                move = b[move]
                if not seen[move]:
                    seen[move] = True
                    heappush(pq, [cnt+1, -move])

        return -1
