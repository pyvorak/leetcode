class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0
        l = 1
        r = sum(candies) // k

        candies.sort(reverse = True)

        def check(m):
            cnt = 0

            for candy in candies:
                if candy < m:
                    break
                cnt += candy // m
                if cnt >= k:
                    return True
            
            return cnt >= k


        while l <= r:
            m = (l+r)//2
            if check(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans
