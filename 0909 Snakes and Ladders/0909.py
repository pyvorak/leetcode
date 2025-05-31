class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board) 

        b = [-1]
        flip = False

        for row in board[::-1]:
            if flip:
                b.extend(row[::-1])
            else:
                b.extend(row)
            flip = not flip
        
        b = [x if x != -1 else i for i, x in enumerate(b)]

        pq = [(0, -1)]
        seen = [False] * (n*n+1)
        n2 = n*n
    
        while pq:
            cnt, x = heappop(pq)
            x = -x

            if x == n2:
                return cnt

            for move in range(x+1, min(x+6, n2)+1):
                move = b[move]
                if not seen[move]:
                    seen[move] = True
                    heappush(pq, [cnt+1, -move])

        return -1
