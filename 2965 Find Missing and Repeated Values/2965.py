class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a = None
        b = set(range(1, n**2+1))
        
        for row in grid:
            for num in row:
                if num not in b:
                    a = num
                else:
                    b.remove(num)

        return [a, list(b)[0]]
