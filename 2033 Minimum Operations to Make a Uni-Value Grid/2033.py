class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = sorted(x for row in grid for x in row)
        
        if (a[-1] - a[0]) % x != 0:
            return -1 
        
        ans = 0
        
        m = a[len(a) // 2]
        
        for num in a:
            d = abs(m - num)
            if d % x != 0:
                return -1   
            else:
                ans += d // x
        
        return ans
