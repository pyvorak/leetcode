class Solution:
    def canChange(self, start: str, target: str) -> bool:        
        l, r = 0, 0
        n = len(start)

        for i in range(n):
            a, b = start[i], target[i]
            
            if a == 'R':
                r += 1
            if b == 'L':
                l += 1
            
            if a == 'L':
                if l <= 0 or r > 0:
                    return False
                else:
                    l -= 1
            if b == 'R':
                if r <= 0 or l > 0:
                    return False
                else:
                    r -= 1

        return l == r == 0
