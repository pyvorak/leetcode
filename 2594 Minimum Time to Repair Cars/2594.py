class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort(reverse = True) 
        l = 0
        ans = r = ranks[0] * cars ** 2
        n = len(ranks)

        def valid(m):
            cnt = 0

            for r in ranks:
                cnt += int(math.sqrt(m // r))
                if cnt >= cars:
                    return True 

            return cnt >= cars

        while l <= r:
            m = (l + r) // 2
            if valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans

        
